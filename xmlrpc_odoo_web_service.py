import xmlrpc.client

url = "http://localhost:8069"
db = 'schooldb1'
username = 'admin'
password = 'admin'

try:

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    if uid:
        print("Authentication succeeded")
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        # Read method
        model = 'school.student'  
        fields = ['name', 'phone']  
        domain = []  # [('field', '=', 'value')])
        limit = 5 
        records = models.execute_kw(db, uid, password, model, 'search_read', [domain], {'fields': fields, 'limit': limit})
        # Print the fetched records
        for record in records:
            print(record)
            
        #Create Method
        my_data={'name' : 'Aman Deep Singh', 'phone':'9872452309','email_parent':'amandeep.singh@brainvire.com'}
        to_create = models.execute_kw(db, uid, password, model, 'create', [my_data])
        print(f"Created record with {id} = ",to_create)
        
        #Unlink Method
        my_data=[17]
        to_unlink = models.execute_kw(db, uid, password, model, 'unlink', [my_data])
        print(f"Deleted record with {id} = ",to_unlink)
    else:
        print("Authentication Failed")
        
except Exception as e:
    print("Error:", e)

