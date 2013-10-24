# -*- coding: utf-8 -*-
"""
    sphinx.domains.chaos
    ~~~~~~~~~~~~~~~~~~~~~

    The CHAOS domain.

    :copyright: Copyright 2007-2013 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.compat import Directive
from sphinx.util.docfields import Field, GroupedField, TypedField


class AuthField(TypedField):
    '''
    A field for specifying required authentication for Actions in CHAOS.

    Inspired by:
    https://github.com/deceze/Sphinx-HTTP-domain/blob/master/sphinx_http_domain/docfields.py
    (David Zentgraf, BSD License... hmmm, should I include his license?)
    '''

    # List of authentication types for actions
    auth_help_msgs = {
        # 'field_name': ('Displayed title', 'Displayed description'),
        'logged_in': ('Logged in', 'You need to be logged in to use this feature'),
        'system_manage_permission': ('Manage permission', 'Requires the SystemPermissons.Manage permission'),
        'user_manager_permission': ('UserManager permission', 'Requires the SystemPermissons.UserManager permission'),
        'create_group_permission': ('CreateGroup permission', 'Requires the SystemPermissons.CreateGroup permission'),
    }

    def default_content(self, fieldarg):
        """
        Given a fieldarg, returns the status code description in list form.

        The default status codes are provided in self.status_codes.
        """
        try:
            return (nodes.Text(f) for f in self.auth_help_msgs[fieldarg])
        except KeyError:
            ### Old version raises exception on non-existent entries
            ## import inspect
            ## frame = inspect.currentframe()
            ## filename = frame.f_code.co_filename
            ## line = frame.f_lineno
            ## raise Exception(
            ##           ('The authentication spec "%s" could not be found.\n'
            ##            'Either fix the spelling error, or add it to the list in '
            ##            'this Python file (%s around line %u).') % (fieldarg, filename, line)
            ##       )
            # If no entry is found just replace underscores with spaces in the
            # name
            fieldarg_spaces = fieldarg.replace('_', ' ')
            return (nodes.Text(fieldarg_spaces), '')

    def make_entry(self, fieldarg, content):
        # Wrap Field.make_entry, but intercept empty content and replace
        # it with default content.
        name, default_content = self.default_content(fieldarg)
        if content.astext() == '':
            content = default_content
        return super(TypedField, self).make_entry(name, content)


class OptAuthField(AuthField):
    # List of authentication types for actions
    auth_help_msgs = {
        # 'field_name': ('Displayed title', 'Displayed description'),
        'logged_in': ('Logged in', 'You may need to be logged in to use this feature'),
        'system_manage_permission': ('Manage permission', 'May require the SystemPermissons.Manage permission'),
        'user_manager_permission': ('UserManager permission', 'May require the SystemPermissons.UserManager permission'),
    }


class CHAOSObject(ObjectDescription):
    """
    Description of a general CHAOS object.
    """
    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
        'annotation': directives.unchanged,
    }

    doc_field_types = [
        TypedField('parameter', label=l_('Parameters'),
                   names=('param', 'parameter', 'arg', 'argument',
                          'keyword', 'kwarg', 'kwparam'),
                   typerolename='type', typenames=('paramtype', 'type'),
                   can_collapse=True),
        TypedField('variable', label=l_('Variables'), rolename='obj',
                   names=('var', 'ivar', 'cvar'),
                   typerolename='obj', typenames=('vartype',),
                   can_collapse=True),
        GroupedField('exceptions', label=l_('Raises'), rolename='exc',
                     names=('raises', 'raise', 'exception', 'except'),
                     can_collapse=True),
        Field('returnvalue', label=l_('Returns'), has_arg=False,
              names=('returns', 'return')),
        Field('returntype', label=l_('Return type'), has_arg=False,
              names=('rtype',)),
        GroupedField('formparameter', label='Form Parameters',
                     names=('formparameter', 'formparam', 'fparam', 'form')),
        AuthField('auth',
                  label='Authentication',
                  names=('auth', 'authentication'),
                  # typerolename='authnote', typenames=('authtype', 'authnote')
                 ),
        OptAuthField('optauth',
                  label='Optional authentication',
                  names=('optauth', 'optional_authentication'),
                  # typerolename='authnote', typenames=('authtype', 'authnote')
                 ),
    ]

    def get_signature_postfix(self, sig):
        """May return a postfix to put before the object name in the
        signature.
        """
        return ''

    def handle_signature(self, sig, signode):
        """Transform a CHAOS signature into RST nodes.

        Return (fully qualified name of the thing, classname if any).

        If inside a class, the current class name is handled intelligently:
        * it is stripped from the displayed name if present
        * it is added to the full name (return value) if not present
        """

        # Syntax for CHAOS reference/module/extension/action signatures
        py_sig_re = re.compile(
            r'''^
                ([\w.]*\/)? # <extension>/ (maybe)
                (\w+)  \s*  # <action>
                $           # and nothing more
                ''', re.VERBOSE)

        m = py_sig_re.match(sig)
        if m is None:
            raise ValueError
        name_prefix, name = m.groups()

        # determine module and class name (if applicable), as well as full name
        modname = self.options.get('module', self.env.temp_data.get('chaos:module'))
        extname = self.env.temp_data.get('chaos:extension')
        if extname:
            add_module = False
            if name_prefix and name_prefix.startswith(extname):
                fullname = name_prefix + name
                # class name is given again in the signature
                name_prefix = name_prefix[len(extname):].lstrip('.')
            elif name_prefix:
                # class name is given in the signature, but different
                # (shouldn't happen)
                fullname = extname + '/' + name_prefix + name
            else:
                # class name is not given in the signature
                fullname = extname + '/' + name
        else:
            add_module = True
            if name_prefix:
                extname = name_prefix.rstrip('.')
                fullname = name_prefix + name
            else:
                extname = ''
                fullname = name

        signode['module'] = modname
        signode['extension'] = extname
        signode['fullname'] = fullname


        if name_prefix:
            signode += addnodes.desc_addname(name_prefix, name_prefix)
        # exceptions are a special case, since they are documented in the
        # 'exceptions' module.
        elif add_module and self.env.config.add_module_names:
            modname = self.options.get('module', self.env.temp_data.get('chaos:module'))
            if modname and modname != 'exceptions':
                pass
                # Write <Module>/<Extension>
                # nodetext = modname + '/'
                # signode += addnodes.desc_addname(nodetext, nodetext)


        # Add "<Extension_name>/" to the name
        if extname:
            signode += addnodes.desc_addname(extname + '/', extname + '/')
        # Write actual name of the thing
        signode += addnodes.desc_name(name, name)

        # Add postfix
        sig_postfix = self.get_signature_postfix(sig)
        if sig_postfix:
            signode += addnodes.desc_annotation(sig_postfix, sig_postfix)

        # Add full description text (called annotation)
        anno = self.options.get('annotation')
        if anno:
            signode += addnodes.desc_annotation(' ' + anno, ' ' + anno)
        return fullname, name_prefix

    def get_index_text(self, modname, name):
        """Return the text for the index entry of the object."""
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        modname = self.options.get(
            'module', self.env.temp_data.get('chaos:module'))
        fullname = (modname and modname + '.' or '') + name_cls[0]
        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['chaos']['objects']
            if fullname in objects:
                self.state_machine.reporter.warning(
                    'duplicate object description of %s, ' % fullname +
                    'other instance in ' +
                    self.env.doc2path(objects[fullname][0]) +
                    ', use :noindex: for one of them',
                    line=self.lineno)
            objects[fullname] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(modname, name_cls)
        if indextext:
            self.indexnode['entries'].append(('single', indextext,
                                              fullname, ''))

    def before_content(self):
        # needed for automatic qualification of members (reset in subclasses)
        self.clsname_set = False

    def after_content(self):
        if self.clsname_set:
            self.env.temp_data['chaos:extension'] = None


class CHAOSModulelevel(CHAOSObject):
    """
    Description of an object on module level (functions, data).
    """

    def get_index_text(self, modname, name_cls):
        if self.objtype == 'function':
            if not modname:
                return _('%s() (built-in function)') % name_cls[0]
            return _('%s() (in module %s)') % (name_cls[0], modname)
        elif self.objtype == 'data':
            if not modname:
                return _('%s (built-in variable)') % name_cls[0]
            return _('%s (in module %s)') % (name_cls[0], modname)
        else:
            return ''


class CHAOSClasslike(CHAOSObject):
    """
    Description of a class-like object (classes, interfaces, exceptions).
    """

    def get_signature_postfix(self, sig):
        return ' ' + self.objtype

    def get_index_text(self, modname, name_cls):
        if self.objtype == 'class':
            if not modname:
                return _('%s (built-in class)') % name_cls[0]
            return _('%s (class in %s)') % (name_cls[0], modname)
        elif self.objtype == 'exception':
            return name_cls[0]
        else:
            return ''

    def before_content(self):
        CHAOSObject.before_content(self)
        if self.names:
            self.env.temp_data['chaos:extension'] = self.names[0][0]
            self.clsname_set = True


class CHAOSClassmember(CHAOSObject):
    """
    Description of a class member (methods, attributes).
    """

    def get_signature_prefix(self, sig):
        return ''

    def get_index_text(self, modname, name_cls):
        name, cls = name_cls
        add_modules = self.env.config.add_module_names
        if self.objtype == 'method':
            try:
                clsname, methname = name.rsplit('/', 1)
            except ValueError:
                if modname:
                    return _('%s() (in module %s)') % (name, modname)
                else:
                    return '%s()' % name
            if modname and add_modules:
                return _('%s() (%s.%s method)') % (methname, modname, clsname)
            else:
                return _('%s() (%s method)') % (methname, clsname)
        elif self.objtype == 'attribute':
            try:
                clsname, attrname = name.rsplit('.', 1)
            except ValueError:
                if modname:
                    return _('%s (in module %s)') % (name, modname)
                else:
                    return name
            if modname and add_modules:
                return _('%s (%s.%s attribute)') % (attrname, modname, clsname)
            else:
                return _('%s (%s attribute)') % (attrname, clsname)
        else:
            return ''

    def before_content(self):
        CHAOSObject.before_content(self)
        lastname = self.names and self.names[-1][1]
        if lastname and not self.env.temp_data.get('chaos:extension'):
            self.env.temp_data['chaos:extension'] = lastname.strip('.')
            self.clsname_set = True


class CHAOSModule(CHAOSObject):
    """
    Directive to mark description of a new module.
    """

    def get_signature_postfix(self, sig):
        return ' ' + self.objtype

    def get_index_text(self, modname, name):
        return _('%s (Module)') % name[0]

    def before_content(self):
        CHAOSObject.before_content(self)
        lastname = self.names and self.names[-1][1]
        if lastname and not self.env.temp_data.get('chaos:extension'):
            self.env.temp_data['chaos:extension'] = lastname.strip('.')
            self.clsname_set = True

    def run(self):
        env = self.state.document.settings.env
        modname = self.arguments[0].strip()
        noindex = 'noindex' in self.options
        env.temp_data['chaos:module'] = modname
        ret = CHAOSObject.run(self)
        if not noindex:
            env.domaindata['chaos']['modules'][modname] = \
                (env.docname, self.options.get('synopsis', ''),
                 self.options.get('platform', ''), 'deprecated' in self.options)
            # make a duplicate entry in 'objects' to facilitate searching for
            # the module in CHAOSDomain.find_obj()
            env.domaindata['chaos']['objects'][modname] = (env.docname, 'module')
            targetnode = nodes.target('', '', ids=['module-' + modname],
                                      ismod=True)
            self.state.document.note_explicit_target(targetnode)
            # the platform and synopsis aren't printed; in fact, they are only
            # used in the modindex currently
            ret.append(targetnode)
            indextext = _('%s (module)') % modname
            inode = addnodes.index(entries=[('single', indextext,
                                             'module-' + modname, '')])
            ret.append(inode)
        return ret


class CHAOSCurrentModule(Directive):
    """
    This directive is just to tell Sphinx that we're documenting
    stuff in module foo, but links to module foo won't lead here.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        env = self.state.document.settings.env
        modname = self.arguments[0].strip()
        if modname == 'None':
            env.temp_data['chaos:module'] = None
        else:
            env.temp_data['chaos:module'] = modname
        return []


class CHAOSXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['chaos:module'] = env.temp_data.get('chaos:module')
        refnode['chaos:extension'] = env.temp_data.get('chaos:extension')
        if not has_explicit_title:
            title = title.lstrip('.')   # only has a meaning for the target
            target = target.lstrip('~') # only has a meaning for the title
            # if the first character is a tilde, don't display the module/class
            # parts of the contents
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('.')
                if dot != -1:
                    title = title[dot+1:]
        # if the first character is a dot, search more specific namespaces first
        # else search builtins first
        if target[0:1] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target


class CHAOSModuleIndex(Index):
    """
    Index subclass to provide the CHAOS module index.
    """

    name = 'modindex'
    localname = l_('CHAOS Module Index')
    shortname = l_('modules')

    def generate(self, docnames=None):
        content = {}
        # list of prefixes to ignore
        ignores = self.domain.env.config['modindex_common_prefix']
        ignores = sorted(ignores, key=len, reverse=True)
        # list of all modules, sorted by module name
        modules = sorted(self.domain.data['modules'].iteritems(),
                         key=lambda x: x[0].lower())
        # sort out collapsable modules
        prev_modname = ''
        num_toplevels = 0
        for modname, (docname, synopsis, platforms, deprecated) in modules:
            if docnames and docname not in docnames:
                continue

            for ignore in ignores:
                if modname.startswith(ignore):
                    modname = modname[len(ignore):]
                    stripped = ignore
                    break
            else:
                stripped = ''

            # we stripped the whole module name?
            if not modname:
                modname, stripped = stripped, ''

            entries = content.setdefault(modname[0].lower(), [])

            package = modname.split('.')[0]
            if package != modname:
                # it's a submodule
                if prev_modname == package:
                    # first submodule - make parent a group head
                    if entries:
                        entries[-1][1] = 1
                elif not prev_modname.startswith(package):
                    # submodule without parent in list, add dummy entry
                    entries.append([stripped + package, 1, '', '', '', '', ''])
                subtype = 2
            else:
                num_toplevels += 1
                subtype = 0

            qualifier = deprecated and _('Deprecated') or ''
            entries.append([stripped + modname, subtype, docname,
                            'module-' + stripped + modname, platforms,
                            qualifier, synopsis])
            prev_modname = modname

        # apply heuristics when to collapse modindex at page load:
        # only collapse if number of toplevel modules is larger than
        # number of submodules
        collapse = len(modules) - num_toplevels < num_toplevels

        # sort by first letter
        content = sorted(content.iteritems())

        return content, collapse


class CHAOSDomain(Domain):
    """CHAOS language domain."""
    name = 'chaos'
    label = 'chaos'
    object_types = {
        'module':       ObjType(l_('module'),        'mod', 'obj'),
        'extension':    ObjType(l_('extension'),     'ext', 'obj'),
        'action':       ObjType(l_('action'),        'act', 'obj'),

        'data':         ObjType(l_('data'),          'data', 'obj'),
        'exception':    ObjType(l_('exception'),     'exc',  'obj'),
        'method':       ObjType(l_('method'),        'meth', 'obj'),
        'attribute':    ObjType(l_('attribute'),     'attr', 'obj'),
    }

    directives = {
        'module':          CHAOSModule,
        'extension':       CHAOSClasslike,
        'action':          CHAOSClassmember,

        'function':        CHAOSModulelevel,
        'data':            CHAOSModulelevel,
        'exception':       CHAOSClasslike,
        'attribute':       CHAOSClassmember,
        'currentmodule':   CHAOSCurrentModule,
    }
    roles = {
        'mod':   CHAOSXRefRole(),
        'ext':   CHAOSXRefRole(),
        'act':   CHAOSXRefRole(),

        'data':  CHAOSXRefRole(),
        'exc':   CHAOSXRefRole(),
        'func':  CHAOSXRefRole(),
        'const': CHAOSXRefRole(),
        'attr':  CHAOSXRefRole(),
        'obj':   CHAOSXRefRole(),
    }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
        'modules': {},  # modname -> docname, synopsis, platform, deprecated
    }
    indices = [
        CHAOSModuleIndex,
    ]

    def clear_doc(self, docname):
        for fullname, (fn, _) in self.data['objects'].items():
            if fn == docname:
                del self.data['objects'][fullname]
        for modname, (fn, _, _, _) in self.data['modules'].items():
            if fn == docname:
                del self.data['modules'][modname]

    def find_obj(self, env, modname, extname, name, type, searchmode=0):
        """Find a CHAOS object for "name", perhaps using the given module
        and/or extname.  Returns a list of (name, object entry) tuples.
        """
        # skip parens
        if name[-2:] == '()':
            name = name[:-2]

        if not name:
            return []

        objects = self.data['objects']
        matches = []

        newname = None
        if searchmode == 1:
            objtypes = self.objtypes_for_role(type)
            if objtypes is not None:
                if modname and extname:
                    fullname = modname + '.' + extname + '/' + name
                    if fullname in objects and objects[fullname][1] in objtypes:
                        newname = fullname
                if not newname:
                    if modname and modname + '.' + name in objects and \
                       objects[modname + '.' + name][1] in objtypes:
                        newname = modname + '.' + name
                    elif name in objects and objects[name][1] in objtypes:
                        newname = name
                    else:
                        # "fuzzy" searching mode
                        searchname = '.' + name
                        matches = [(oname, objects[oname]) for oname in objects
                                   if oname.endswith(searchname)
                                   and objects[oname][1] in objtypes]
        else:
            # NOTE: searching for exact match, object type is not considered
            if name in objects:
                newname = name
            elif type == 'mod':
                # only exact matches allowed for modules
                return []
            regex = re.compile(r'.*%s' % name)
            key_matches = filter(regex.match, objects.keys())
            matches = [(key, objects[key]) for key in key_matches]
            # elif extname and extname + '/' + name in objects:
            #     newname = extname + '/' + name
            # elif modname and modname + '.' + name in objects:
            #     newname = modname + '.' + name
            # elif modname and extname and \
            #          modname + '.' + extname + '.' + name in objects:
            #     newname = modname + '.' + extname + '.' + name
            # # special case: builtin exceptions have module "exceptions" set
            # elif type == 'exc' and '.' not in name and \
            #      'exceptions.' + name in objects:
            #     newname = 'exceptions.' + name
            # # special case: object methods
            # elif type in ('func', 'meth') and '.' not in name and \
            #      'object.' + name in objects:
            #     newname = 'object.' + name
        if newname is not None:
            matches.append((newname, objects[newname]))
        return matches

    def resolve_xref(self, env, fromdocname, builder,
                     type, target, node, contnode):
        modname = node.get('chaos:module')
        extname = node.get('chaos:extension')
        searchmode = node.hasattr('refspecific') and 1 or 0
        matches = self.find_obj(env, modname, extname, target, type, searchmode)
        if not matches:
            if type != 'type':
                env.warn_node('No match found for cross-reference: %r. (Searchmode: %s)' % (target, searchmode), node)
            return None
        elif len(matches) > 1:
            env.warn_node(
                'more than one target found for cross-reference '
                '%r: %s' % (target, ', '.join(match[0] for match in matches)),
                node)
        name, obj = matches[0]

        if obj[1] == 'module':
            # get additional info for modules
            docname, synopsis, platform, deprecated = self.data['modules'][name]
            assert docname == obj[0]
            title = name
            if synopsis:
                title += ': ' + synopsis
            if deprecated:
                title += _(' (deprecated)')
            if platform:
                title += ' (' + platform + ')'
            return make_refnode(builder, fromdocname, docname,
                                'module-' + name, contnode, title)
        else:
            return make_refnode(builder, fromdocname, obj[0], name,
                                contnode, name)

    def get_objects(self):
        for modname, info in self.data['modules'].iteritems():
            yield (modname, modname, 'module', info[0], 'module-' + modname, 0)
        for refname, (docname, type) in self.data['objects'].iteritems():
            if type != 'module':  # modules are already handled
                yield (refname, refname, type, docname, refname, 1)

# Extension setup method
def setup(app):
    app.add_domain(CHAOSDomain)
