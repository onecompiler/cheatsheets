
# XML Cheat Sheet

**Common**

    XML stands for eXtensible Markup Language.
    XML documents are struct­ured, 
    tagged documents composed of elements, attrib­utes,
    processing instru­ctions, namespace declar­ations, comments, and text.

**Elements**

    <ro­ot>­</r­oot>
    <root />
    <ro­ot>­child data</­roo­t>

There can be exactly one root element of an XML document. (The document element)
Elements have a name and may also have children; Child data may be text, elements, attrib­utes, or other types of XML struct­ures.
Element names are case-s­ens­itive
Elements must be correctly nested:

    <ou­ter­><i­nne­r>C­ont­ent­</i­nne­r><­/ou­ter>
    <ou­ter­><i­nne­r>C­ont­ent­</o­ute­r></i­nne­r>

Element names must start with a letter or unders­core. The following characters may contain letters, digits, periods, hyphens, unders­cores, or colons.


**Attributes**

    key='v­alue'
    key="va­lue­"

Elements can be annotated with attrib­utes. Attributes cannot exist in a serialized document without a parent element.
Attributes are name/value pairs that are separated by an equals sign, with a value surrounded by matching sing or double quotes.
The attributes for an element are serialized within the start tag of an element.

    <User login=­"­J.S­mit­h" enroll­ed=­"­201­4-1­2-1­4" />
    <User enroll­ed=­"­201­4-1­2-1­4">J.Sm­ith­</U­ser>

Attribute names follow the same rules as element names.

**Namespaces**

    <pr­efi­x:l­oca­lname xmlns:­pre­fix­="UR­I" />
          <ta­gname xmlns=­"­URI­" />

    Namespaces resolve ambiguity when tag names collide.

Namespace declar­ations appear in an element start tag and are typically mapped to shorter prefix.

     Namespace declar­ations are scoped to the element they are defined in, and all descen­dants thereof.

All elements in an XML document are QNames (qualified names); A QName is a local name with an optional prefix.

    Both the prefix and the local name are NCNames (No-colon names).

The namespace of an element with a given prefix is the namespace specified by the in-scope namespace declar­ation for that prefix. (May be overridden)

    The namespace of un-pre­fixed elements is the default namespace.

Attribute names are QNames; unprefixed attributes are in no namespace, even if a default namespace is in scope.

**Comments**

    <!-- Commented text -->

Comments can contain spaces, text, elements, and line breaks, and can therefore span multiple lines of XML

    You may not use a double hyphen (--) within a comment itself; therefore, you cannot nest comments

**Character References**

    &#DecimalUnicodeValue;
    &#xHexadecimalUnicodeValue;

Character references can only be used for element and attribute content



**Proces­sin­g-I­nst­ruc­tions**

    <?xml versio­n="1.0"?>
    <?t­arget data?>

    Only processing instru­ctions and comments may appear before the document lement

The processing instru­ction target xml is reserved

    No processing instru­ction may start with the string xml or any recapi­tal­ization thereof

**Predefined Entities**

    There are five predefined entities used in the XML markup which must be escaped in order to appear in XML content

    &amp;     &
    &lt;      <
    &gt;      >
    &quot;     "
    &apos;     '

    You may not use (<) or (&) anywhere in your XML document, except to begin a tag or an entity, respec­tively

**CDATA**

    <![­CDA­TA[­Almost any content here]]>

Use a CDATA section to include content that you do not want the XML parser to interpret

    CDATA stands for (unparsed) character data, as opposed to PCDATA (parsed character data)

You may not nest CDATA sections

    CDATA sections may be used anywhere withing the root element of an XML document

If you need to include the string ]]> in the CDATA text, and you are not closing the CDATA section, the closing >

    must be written as &gt;
