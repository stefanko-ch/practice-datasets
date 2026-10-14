# AdventureWorks – sales database of a bike manufacturer (11 tables)

The classic Microsoft sample database as CSV files `<Schema>.<Table>.csv`: persons, addresses, products and categories, customers, sales orders and order lines, sales territories. Ideal for JOINs, aggregations and star-schema exercises.

| | |
|---|---|
| Download | [`adventureworks.zip`](https://github.com/stefanko-ch/practice-datasets/releases/download/v1/adventureworks.zip) (8.7 MB) |
| Rows | see below |
| Source | [https://github.com/microsoft/sql-server-samples](https://github.com/microsoft/sql-server-samples) |
| License | MIT (Microsoft sql-server-samples) |

## Sample

### Files in the ZIP

| File | Size |
|---|---|
| `Person.Address.csv` | 19,614 rows |
| `Person.CountryRegion.csv` | 238 rows |
| `Person.Person.csv` | 19,972 rows |
| `Person.StateProvince.csv` | 181 rows |
| `Production.Product.csv` | 504 rows |
| `Production.ProductCategory.csv` | 4 rows |
| `Production.ProductSubcategory.csv` | 37 rows |
| `Sales.Customer.csv` | 19,820 rows |
| `Sales.SalesOrderDetail.csv` | 121,317 rows |
| `Sales.SalesOrderHeader.csv` | 31,465 rows |
| `Sales.SalesTerritory.csv` | 10 rows |

### Sample extract of `Production.Product.csv` (first 10 rows)

| ProductID | Name | ProductNumber | MakeFlag | FinishedGoodsFlag | Color | SafetyStockLevel | ReorderPoint | StandardCost | ListPrice | Size | SizeUnitMeasureCode | WeightUnitMeasureCode | Weight | DaysToManufacture | ProductLine | Class | Style | ProductSubcategoryID | ProductModelID | SellStartDate | SellEndDate | DiscontinuedDate | rowguid | ModifiedDate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Adjustable Race | AR-5381 | 0 | 0 |  | 1000 | 750 | 0.0 | 0.0 |  |  |  |  | 0 |  |  |  |  |  | 2008-04-30 00:00:00.000 |  |  | 694215B7-08F7-4C0D-ACB1-D734BA44C0C8 | 2014-02-08 10:01:36.827 |
| 2 | Bearing Ball | BA-8327 | 0 | 0 |  | 1000 | 750 | 0.0 | 0.0 |  |  |  |  | 0 |  |  |  |  |  | 2008-04-30 00:00:00.000 |  |  | 58AE3C20-4F3A-4749-A7D4-D568806CC537 | 2014-02-08 10:01:36.827 |
| 3 | BB Ball Bearing | BE-2349 | 1 | 0 |  | 800 | 600 | 0.0 | 0.0 |  |  |  |  | 1 |  |  |  |  |  | 2008-04-30 00:00:00.000 |  |  | 9C21AED2-5BFA-4F18-BCB8-F11638DC2E4E | 2014-02-08 10:01:36.827 |
| 4 | Headset Ball Bearings | BE-2908 | 0 | 0 |  | 800 | 600 | 0.0 | 0.0 |  |  |  |  | 0 |  |  |  |  |  | 2008-04-30 00:00:00.000 |  |  | ECFED6CB-51FF-49B5-B06C-7D8AC834DB8B | 2014-02-08 10:01:36.827 |
| 316 | Blade | BL-2036 | 1 | 0 |  | 800 | 600 | 0.0 | 0.0 |  |  |  |  | 1 |  |  |  |  |  | 2008-04-30 00:00:00.000 |  |  | E73E9750-603B-4131-89F5-3DD15ED5FF80 | 2014-02-08 10:01:36.827 |
| 317 | LL Crankarm | CA-5965 | 0 | 0 | Black | 500 | 375 | 0.0 | 0.0 |  |  |  |  | 0 |  | L  |  |  |  | 2008-04-30 00:00:00.000 |  |  | 3C9D10B7-A6B2-4774-9963-C19DCEE72FEA | 2014-02-08 10:01:36.827 |
| 318 | ML Crankarm | CA-6738 | 0 | 0 | Black | 500 | 375 | 0.0 | 0.0 |  |  |  |  | 0 |  | M  |  |  |  | 2008-04-30 00:00:00.000 |  |  | EABB9A92-FA07-4EAB-8955-F0517B4A4CA7 | 2014-02-08 10:01:36.827 |
| 319 | HL Crankarm | CA-7457 | 0 | 0 | Black | 500 | 375 | 0.0 | 0.0 |  |  |  |  | 0 |  |  |  |  |  | 2008-04-30 00:00:00.000 |  |  | 7D3FD384-4F29-484B-86FA-4206E276FE58 | 2014-02-08 10:01:36.827 |
| 320 | Chainring Bolts | CB-2903 | 0 | 0 | Silver | 1000 | 750 | 0.0 | 0.0 |  |  |  |  | 0 |  |  |  |  |  | 2008-04-30 00:00:00.000 |  |  | 7BE38E48-B7D6-4486-888E-F53C26735101 | 2014-02-08 10:01:36.827 |
| 321 | Chainring Nut | CN-6137 | 0 | 0 | Silver | 1000 | 750 | 0.0 | 0.0 |  |  |  |  | 0 |  |  |  |  |  | 2008-04-30 00:00:00.000 |  |  | 3314B1D7-EF69-4431-B6DD-DC75268BD5DF | 2014-02-08 10:01:36.827 |
