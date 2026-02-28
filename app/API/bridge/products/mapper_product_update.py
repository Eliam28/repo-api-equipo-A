def product_update(id, active, name, slug, reference):
    xml = f"""
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
      <product>
        <id>{id}</id>
        <active>{active}</active>


        <name>
          <language id="1"><![CDATA[{name}]]></language>
        </name>

        <link_rewrite>
          <language id="1"><![CDATA[{slug}]]></language>
        </link_rewrite>


      </product>
    </prestashop>
    """
    return xml


#        <reference><![CDATA[{reference}]]></reference>
#        <supplier_reference><![CDATA[{reference}]]></supplier_reference>
#        <meta_title>
#          <language id="1"><![CDATA[{name}]]></language>
#        </meta_title>