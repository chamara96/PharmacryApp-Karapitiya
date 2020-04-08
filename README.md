# PharmacryApp (Karapitiya) DJango Python Backend

# MDS
Medicine Delivery System

## API (Debug = True)
> Last update - 2020-04-06 <br>
http://python.chamaralabs.com/

### Testing Python host (Debug = True)
Link http://python.chamaralabs.com/clientuser/


#### Login
```bash
http://python.chamaralabs.com/login/<username>&<password>
```
#### Registation (Client)
```bash
http://python.chamaralabs.com/clientuser/reg/<name>&<phonenumber>&<latitude>&<longidute>&<address>&<password>
```
#### Registation (Pharmacy)
```bash
http://python.chamaralabs.com/pharmuser/reg/<name>&<owner>&<phonenumber>&<latitude>&<longidute>&<address>&<password>
```
#### Get nearest pharmacy list (Client)
```bash
http://python.chamaralabs.com/clientuser/pharmlist/<userid>/<latitude>&<longidute>
```
#### Set Order (Client)
```bash
http://python.chamaralabs.com/clientuser/setorder/<userid>/<pharmacy id list>
```

#### View Order (Pharm)
```bash
http://python.chamaralabs.com/pharmuser/vieworder/<userid>/<query>
```
#### Get Order (Pharm)
```bash
http://python.chamaralabs.com/pharmuser/getorder/<userid>/<order_id>
```
