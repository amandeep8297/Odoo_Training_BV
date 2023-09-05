# Odoo_Training_BV

# School Management System

## View:
[![Project Image or Logo](https://drive.google.com/uc?export=view&id=1KP0FA2uFsDR67PAK_CrsY_B45x_5FJjY)](project_url)


## About
School management system is learning project as a trainee, so here are some of the highlights and salient features:

## Language used:
Oddo, Python3, XML
 
## Backend Work

- [ Create and manage student details, parent details, class teachers in a central database](#features)
- [Can see views in Tree, Form, Kanban, Pivot.](#getting-started)
- [Generate QWeb reports of students ID-Card and Xlsx report of selected records. ](#usage)
- [Cron job like sending mails.](#contributing)
- [ Can Delete Admission of any record using Wizard](#license)



# Extending Point_of_sale Module

## About
Extended existing components of Point of Sale (POS) system, as outlined below:
Default Addons Path: odoo addons > point_of_sale > static > src > js > Screens

## Language used:
Oddo OWL framework, Javascript, XML, Python3

## Frontend Work:

##### Popup Screen:
[![Second Image](https://drive.google.com/uc?export=view&id=1bgIVEkUvksapGf-11ov4ngTHDqCyCgO3)](https://drive.google.com/file/d/1bgIVEkUvksapGf-11ov4ngTHDqCyCgO3/view?usp=sharing)

##### Receipt Screen
[![Third Image](https://drive.google.com/uc?export=view&id=1M0pC6wSs1fHQysRmPjVI-IMXGtHadti9)](https://drive.google.com/file/d/1M0pC6wSs1fHQysRmPjVI-IMXGtHadti9/view?usp=sharing)

#### Worked on Screen Component List :
1. ClientListScreen
2. PaymentScreen
3. ProductScreen

### Task performed on the following functionalities:
#### -> Mobile Number Field Integration:
   - Integrated a unique mobile number field in the POS to be stored in the backend.
   - Ensured each mobile number is unique for every customer.
   - Displayed the mobile number field in the List view of customer selections within the POS.
   - Included the mobile number in the POS Receipt screen.

#### -> Popup Text Box Addition at POS Order Level:
   - Implemented a popup text box at the POS order level, with the text value stored in the backend POS order.
   - Preserved the entered text value even if the popup is closed or the user navigates within the shop.
   - Printed the stored text value in the POS receipt.

#### -> Enforce Customer Selection Before Order Proceeds:
   - Restrict order processing without a customer selection.
   - If the Payment button is clicked and no customer is selected, trigger a user error.








