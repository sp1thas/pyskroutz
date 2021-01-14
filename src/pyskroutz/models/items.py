from marshmallow import Schema, fields


class WebUriItem(Schema):
    web_uri = fields.Url()


class ItemBase(Schema):
    id = fields.Integer()
    name = fields.String()


class BuyItem(Schema):
    price_min = fields.Float()
    price_max = fields.Float()
    shop_count = fields.Integer()
    reviewscore = fields.Float()
    reviews_count = fields.Integer()
    reviewable = fields.Boolean()


class Category(ItemBase, WebUriItem):
    children_count = fields.Integer()
    image_url = fields.Url()
    parent_id = fields.Integer()
    fashion = fields.Boolean()
    layout_mode = fields.String()
    code = fields.String()
    path = fields.String()
    show_specifications = fields.Boolean()
    manufacturer_title = fields.String()


class ImageItemBase(Schema):
    main = fields.String()
    alternatives = fields.List(fields.String())


class Sku(ItemBase, BuyItem, WebUriItem):
    ean = fields.String()
    pn = fields.String()
    display_name = fields.String()
    category_id = fields.Integer()
    first_product_shop_info = fields.String()
    click_url = fields.Url()
    plain_spec_summary = fields.String()
    manufacturer_id = fields.Integer()
    future = fields.Boolean()
    virtual = fields.Boolean()
    images: fields.List(ImageItemBase)
    favorited: fields.Boolean()
    comparable: fields.Boolean()
    name_source: fields.Boolean()


class Book(ItemBase, BuyItem, WebUriItem):
    main_author_id = fields.Integer()
    main_author = fields.String()
    images = fields.List(ImageItemBase)
