from ...Models.Account import Account as AccountModel

class Account:


    def create_account(self,name,url,password,notes):

        account=AccountModel(name=name,url=url,password=password,notes=notes)
        account.save()
        print(f"account {name} created ")

    def get_account(self,name):
        account=AccountModel.get(AccountModel.name==name)
        if(account):
            print("------Account------")
            print(f"name: {account.name}")
            print(f"url: {account.url}")
            print(f"notes: {account.notes}")
            print()
            
        

    def list_accounts(self):
        accounts=AccountModel.select()
        for a in accounts:
            print("account name"+a.name)

            

        
    