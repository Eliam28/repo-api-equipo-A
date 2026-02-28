def product_update(id, active, price):
    xml = f"""
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
      <product>
        <id>{id}</id>
        <active>{active}</active>
        <price><![CDATA[{price}]]></price>
      </product>
    </prestashop>
    """

    return xml