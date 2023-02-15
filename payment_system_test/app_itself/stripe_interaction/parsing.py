class ApiResponses:

    def product_price(price_info: dict):
        #info_list = list()
        currency = price_info.get('currency')
        price = price_info.get('unit_amount')

        #full_price = f"{price[:-2]}'.'{price[-2:]}{currency}"

        return price[:-2]