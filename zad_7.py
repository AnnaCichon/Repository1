import requests

r = requests.get("https://api.openbrewerydb.org/breweries")
response = r.json()


class Brawery:
    def __init__(self, id: int, name: str, brewery_type: str, street: str, address_2: str, address_3: str, city: str, state: str, county_province: str, postal_code: str, country: str, longitude: str, latitude: str, phone: str, website_url: str, updated_at: str, created_at: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self) -> str:
        return f'id: {self.id}, \n name: {self.name}, \n brewery_type: {self.brewery_type}, \n street: {self.street}, \n address_2: {self.address_2}, \n address_3: {self.address_3}, \n city: {self.city}, \n state: {self.state}, \n county_province: {self.county_province}, \n postal_code: {self.postal_code}, \n country: {self.postal_code}, \n longitude: {self.longitude}, \n latitude: {self.longitude}, \n phone: {self.phone}, \n website_url: {self.website_url}, \n updated_at: {self.updated_at}, \n created_at: {self.created_at} \n'


lista_20 = [Brawery(dict['id'], dict['name'], dict['brewery_type'], dict['street'], dict['address_2'], dict['address_3'], dict['city'], dict['state'], dict['county_province'], dict['postal_code'], dict['country'], dict['longitude'], dict['latitude'], dict['phone'], dict['website_url'], dict['updated_at'], dict['created_at']) for dict in response[0:20]]

for i in lista_20:
    print(i)