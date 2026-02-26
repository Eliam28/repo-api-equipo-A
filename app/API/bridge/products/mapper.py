def odoo_to_prestashop(product):

    name = product["name"]
    price = product["list_price"]
    reference = product["default_code"]

    slug = name.lower().replace(" ", "-")

    xml = f"""
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
      <product>

        <id_shop_default>1</id_shop_default>
        <active>1</active>
        <available_for_order>1</available_for_order>
        <show_price>1</show_price>

        <name>
          <language id="1">{name}</language>
        </name>

        <link_rewrite>
          <language id="1">{slug}</language>
        </link_rewrite>

        <price>{price}</price>
        <reference>{reference}</reference>

        <id_category_default>10</id_category_default>

        <associations>
          <categories>
            <category>
              <id>10</id>
            </category>
          </categories>
        </associations>

      </product>
    </prestashop>
    """

    return xml