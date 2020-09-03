# Shopping app with Qraphql

In this project the graphql api method is applied for getting and posting data. Django is used for handling requests and Database handling.

## Installation
To install this project

```bash
docker-compose build --no-cache
```
In order to run

```bash
docker-compose up
```
Also to stop it
```bash
docker-compose down -v
```

## Usage
in order to see result data in graphql, some dummy data is populated with autofixture in entrypoin.sh with this command:

```bash
python manage.py loadtestdata buy.Orders:3000 buy.Products:2000 -d
```
So to see results follow: 0.0.0.0:8000/graphql

to get data put this as query and press > button. all dummy data is shown.
```json
query{
  allOrders {
    id
    totalPrice
    deliveryMethod
  }
  allProducts{
    category
    id
    name
  }
}
```
for posting order data use this mutation

```json

mutation{
  addOrder(input:{deliveryMethod:"sdssdsdd", paymentMethod: "55sdsd"}){
    order{
      deliveryMethod
      paymentMethod
      products
      quantities
      totalPrice
    }
  }
}

```
and for posting product data:
```json
mutation{
  addProduct(input:{name:"randName",category:"sthiii",quantity:5}){
    product{
      name
      category
      quantity
    }
  }
}
```

## [Medium](https://medium.com/@sdamoosavi/shopping-application-with-django-and-django-graphene-7b47e9d1bf7a)

