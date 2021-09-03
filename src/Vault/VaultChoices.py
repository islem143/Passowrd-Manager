
def create_vault_promts():
    return [{"message":"enter the name of the vault","hidden":False},{
    "message":"enter the masterpassword",
    "hidden":True
}]



INIT_CHOICES={
"1":"create a database/vault",
"2":"connect to a database/vault"
}

# INIT_ACTIONS={
#     "1":init_menu_actions.create_vault,
#     "2":init_menu_actions.connect_to_vault
# }
# INIT_PROMTS={
#     "1":create_vault_promts,
#     "2":create_vault_promts
# }












