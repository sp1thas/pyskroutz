from pySkroutz import Skroutz

# create Skroutz object with your creadentials
skrtz = Skroutz(client_id='your client id', client_secret='your client secret')
# get your access token
print skrtz.access_token
# access token expiration date
print skrtz.access_token_exp
# access token type
print skrtz.access_token_type
