; Module related
(named_module
  name: (long_identifier) @name.definition.module
) @definition.module

(module_defn
  name: (identifier) @name.definition.module
) @definition.module

(namespace
  name: (long_identifier) @name.definition.module
) @definition.module

; Type definitions
(type_definition
   name: (identifier) @name.definition.class
) @definition.class

; Value declarations
(value_declaration
  name: (identifier) @name.definition.method
) @definition.method
