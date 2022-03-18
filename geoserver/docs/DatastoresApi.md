# geoserver.DatastoresApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_datastore**](DatastoresApi.md#create_datastore) | **POST** /workspaces/{workspaceName}/datastores | Create a new data store
[**delete_datastore**](DatastoresApi.md#delete_datastore) | **DELETE** /workspaces/{workspaceName}/datastores/{storeName} | Delete data store
[**get_data_store**](DatastoresApi.md#get_data_store) | **GET** /workspaces/{workspaceName}/datastores/{storeName} | Retrieve a particular data store from a workspace
[**get_datastores**](DatastoresApi.md#get_datastores) | **GET** /workspaces/{workspaceName}/datastores | Get a list of data stores
[**modify_data_store**](DatastoresApi.md#modify_data_store) | **PUT** /workspaces/{workspaceName}/datastores/{storeName} | Modify a data store.

# **create_datastore**
> create_datastore(body, workspace_name)

Create a new data store

Adds a new data store to the workspace.

### Example
```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.DatastoresApi(geoserver.ApiClient(configuration))
body = geoserver.DataStoreInfoWrapper() # DataStoreInfoWrapper | The data store body information to upload. The contents of the connection parameters will differ depending on the type of data store being added.
- GeoPackage


  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "name": "nyc",
        "connectionParameters": {
          "entry": [
            {"@key":"database","$":"file:///path/to/nyc.gpkg"},
            {"@key":"dbtype","$":"geopkg"}
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as 'schema.name' or just 'name' | user | String | False | ` ` |
  | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | ` ` |
  | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | `3` |
  | database | Database | user | File | True | ` ` |
  | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | `1` |
  | fetch size | number of records read with each iteraction with the dbms | user | Integer | False | `1000` |
  | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | `20` |
  | namespace | Namespace prefix | user | String | False | ` ` |
  | max connections | maximum number of open connections | user | Integer | False | `10` |
  | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | `True` |
  | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | `300` |
  | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | ` ` |
  | validate connections | check connection is alive before using it | user | Boolean | False | `True` |
  | dbtype | Type | program | String | True | `geopkg` |
  | passwd | password used to login | user | String | False | ` ` |
  | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | `False` |
  | min connections | minimum number of pooled connection | user | Integer | False | `1` |
  | Evictor run periodicity | number of seconds between idle object evitor runs (default, 300 seconds) | user | Integer | False | `300` |
  | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | ` ` |
  | user | user name to login as | user | String | False | ` ` |

- PostGIS


  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "name": "nyc",
        "connectionParameters": {
          "entry": [
            {"@key":"host","$":"localhost"},
            {"@key":"port","$":"5432"},
            {"@key":"database","$":"nyc"},
            {"@key":"user","$":"bob"},
            {"@key":"passwd","$":"postgres"},
            {"@key":"dbtype","$":"postgis"}
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | `20` |
  | validate connections | check connection is alive before using it | user | Boolean | False | `True` |
  | port | Port | user | Integer | True | `5432` |
  | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as 'schema.name' or just 'name' | user | String | False | ` ` |
  | Support on the fly geometry simplification | When enabled, operations such as map rendering will pass a hint that will enable the usage of ST_Simplify | user | Boolean | False | `True` |
  | create database | Creates the database if it does not exist yet | advanced | Boolean | False | `False` |
  | create database params | Extra specifications appeneded to the CREATE DATABASE command | advanced | String | False | `` |
  | dbtype | Type | program | String | True | `postgis` |
  | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | `1` |
  | namespace | Namespace prefix | user | String | False | ` ` |
  | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | `300` |
  | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | ` ` |
  | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | `False` |
  | min connections | minimum number of pooled connection | user | Integer | False | `1` |
  | Max open prepared statements | Maximum number of prepared statements kept open and cached for each connection in the pool. Set to 0 to have unbounded caching, to -1 to disable caching | user | Integer | False | `50` |
  | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | ` ` |
  | passwd | password used to login | user | String | False | ` ` |
  | encode functions | set to true to have a set of filter functions be translated directly in SQL. Due to differences in the type systems the result might not be the same as evaluating them in memory, including the SQL failing with errors while the in memory version works fine. However this allows to push more of the filter into the database, increasing performance.the postgis table. | advanced | Boolean | False | `False` |
  | host | Host | user | String | True | `localhost` |
  | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | `3` |
  | Loose bbox | Perform only primary filter on bbox | user | Boolean | False | `True` |
  | Evictor run periodicity | number of seconds between idle object evitor runs (default, 300 seconds) | user | Integer | False | `300` |
  | Estimated extends | Use the spatial index information to quickly get an estimate of the data bounds | user | Boolean | False | `True` |
  | database | Database | user | String | False | ` ` |
  | fetch size | number of records read with each iteraction with the dbms | user | Integer | False | `1000` |
  | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | `True` |
  | max connections | maximum number of open connections | user | Integer | False | `10` |
  | preparedStatements | Use prepared statements | user | Boolean | False | `False` |
  | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | ` ` |
  | schema | Schema | user | String | False | `public` |
  | user | user name to login as | user | String | True | ` ` |

- Shapefile


  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "name": "nyc",
        "connectionParameters": {
          "entry": [
            {"@key":"url","$":"file:/path/to/nyc.shp"}
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | `True` |
  | namespace | uri to a the namespace | advanced | URI | False | ` ` |
  | filetype | Discriminator for directory stores | program | String | False | `shapefile` |
  | charset | character used to decode strings from the DBF file | advanced | Charset | False | `ISO-8859-1` |
  | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | `True` |
  | fstype | Enable using a setting of 'shape'. | advanced | String | False | `shape` |
  | url | url to a .shp file | user | URL | True | ` ` |
  | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | `True` |
  | memory mapped buffer | enable/disable the use of memory-mapped io | advanced | Boolean | False | `False` |
  | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | `Pacific Standard Time` |

- Directory of spatial files (shapefiles)


  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "name": "nyc",
        "connectionParameters": {
          "entry": [
            {"@key":"url","$":"file:/path/to/directory"}
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | `True` |
  | namespace | uri to a the namespace | advanced | URI | False | ` ` |
  | filetype | Discriminator for directory stores | program | String | False | `shapefile` |
  | charset | character used to decode strings from the DBF file | advanced | Charset | False | `ISO-8859-1` |
  | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | `True` |
  | fstype | Enable using a setting of 'shape'. | advanced | String | False | `shape` |
  | url | url to a .shp file | user | URL | True | ` ` |
  | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | `True` |
  | memory mapped buffer | enable/disable the use of memory-mapped io | advanced | Boolean | False | `False` |
  | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | `Pacific Standard Time` |


- Web Feature Service


  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "name": "nyc",
        "connectionParameters": {
          "entry": [
            {"@key":"GET_CAPABILITIES_URL","$":"http://localhost:8080/geoserver/wfs?request=GetCapabilities"}
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Protocol | Sets a preference for the HTTP protocol to use when requesting WFS functionality. Set this value to Boolean.TRUE for POST, Boolean.FALSE for GET or NULL for AUTO | user | Boolean | False | ` ` |
  | WFS GetCapabilities URL | Represents a URL to the getCapabilities document or a server instance. | user | URL | False | ` ` |
  | Buffer Size | This allows the user to specify a buffer size in features. This param has a default value of 10 features. | user | Integer | False | `10` |
  | Filter compliance | Level of compliance to WFS specification (0-low,1-medium,2-high) | user | Integer | False | ` ` |
  | EntityResolver | Sets the entity resolver used to expand XML entities | program | EntityResolver | False | `org.geotools.xml.PreventLocalEntityResolver@75e98519` |
  | Time-out | This allows the user to specify a timeout in milliseconds. This param has a default value of 3000ms. | user | Integer | False | `3000` |
  | GmlComplianceLevel | Optional OGC GML compliance level required. | user | Integer | False | `0` |
  | Lenient | Indicates that datastore should do its best to create features from the provided data even if it does not accurately match the schema.  Errors will be logged but the parsing will continue if this is true.  Default is false | user | Boolean | False | `False` |
  | Password | This allows the user to specify a username. This param should not be used without the USERNAME param. | user | String | False | ` ` |
  | Use Default SRS | Use always the declared DefaultSRS for requests and reproject locally if necessary | advanced | Boolean | False | `False` |
  | Namespace | Override the original WFS type name namespaces | advanced | String | False | ` ` |
  | Username | This allows the user to specify a username. This param should not be used without the PASSWORD param. | user | String | False | ` ` |
  | Axis Order Filter | Indicates axis order used by the remote WFS server for filters. It applies only to WFS 1.x.0 servers. Default is the same as AXIS_ORDER | advanced | String | False | ` ` |
  | GmlCompatibleTypeNames | Use Gml Compatible TypeNames (replace : by _). | user | Boolean | False | `False` |
  | Maximum features | Positive integer used as a hard limit for the amount of Features to retrieve for each FeatureType. A value of zero or not providing this parameter means no limit. | user | Integer | False | `0` |
  | Axis Order | Indicates axis order used by the remote WFS server in result coordinates. It applies only to WFS 1.x.0 servers. Default is Compliant | advanced | String | False | `Compliant` |
  | WFS Strategy | Override wfs stragegy with either cubwerx, ionic, mapserver, geoserver, strict, nonstrict or arcgis strategy. | user | String | False | `auto` |
  | Try GZIP | Indicates that datastore should use gzip to transfer data if the server supports it. Default is true | user | Boolean | False | `True` |
  | Encoding | This allows the user to specify the character encoding of the XML-Requests sent to the Server. Defaults to UTF-8 | user | String | False | `UTF-8` |
  | Outputformat | This allows the user to specify an outputFormat, different from the default one. | advanced | String | False | ` ` |

workspace_name = 'workspace_name_example' # str | The name of the worskpace containing the data stores.

try:
    # Create a new data store
    api_instance.create_datastore(body, workspace_name)
except ApiException as e:
    print("Exception when calling DatastoresApi->create_datastore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataStoreInfoWrapper**](DataStoreInfoWrapper.md)| The data store body information to upload. The contents of the connection parameters will differ depending on the type of data store being added.
- GeoPackage


  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;name&quot;: &quot;nyc&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;database&quot;,&quot;$&quot;:&quot;file:///path/to/nyc.gpkg&quot;},
            {&quot;@key&quot;:&quot;dbtype&quot;,&quot;$&quot;:&quot;geopkg&quot;}
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as &#x27;schema.name&#x27; or just &#x27;name&#x27; | user | String | False | &#x60; &#x60; |
  | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | &#x60; &#x60; |
  | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | &#x60;3&#x60; |
  | database | Database | user | File | True | &#x60; &#x60; |
  | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | &#x60;1&#x60; |
  | fetch size | number of records read with each iteraction with the dbms | user | Integer | False | &#x60;1000&#x60; |
  | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | &#x60;20&#x60; |
  | namespace | Namespace prefix | user | String | False | &#x60; &#x60; |
  | max connections | maximum number of open connections | user | Integer | False | &#x60;10&#x60; |
  | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | &#x60;True&#x60; |
  | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | &#x60;300&#x60; |
  | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | &#x60; &#x60; |
  | validate connections | check connection is alive before using it | user | Boolean | False | &#x60;True&#x60; |
  | dbtype | Type | program | String | True | &#x60;geopkg&#x60; |
  | passwd | password used to login | user | String | False | &#x60; &#x60; |
  | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | &#x60;False&#x60; |
  | min connections | minimum number of pooled connection | user | Integer | False | &#x60;1&#x60; |
  | Evictor run periodicity | number of seconds between idle object evitor runs (default, 300 seconds) | user | Integer | False | &#x60;300&#x60; |
  | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | &#x60; &#x60; |
  | user | user name to login as | user | String | False | &#x60; &#x60; |

- PostGIS


  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;name&quot;: &quot;nyc&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;host&quot;,&quot;$&quot;:&quot;localhost&quot;},
            {&quot;@key&quot;:&quot;port&quot;,&quot;$&quot;:&quot;5432&quot;},
            {&quot;@key&quot;:&quot;database&quot;,&quot;$&quot;:&quot;nyc&quot;},
            {&quot;@key&quot;:&quot;user&quot;,&quot;$&quot;:&quot;bob&quot;},
            {&quot;@key&quot;:&quot;passwd&quot;,&quot;$&quot;:&quot;postgres&quot;},
            {&quot;@key&quot;:&quot;dbtype&quot;,&quot;$&quot;:&quot;postgis&quot;}
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | &#x60;20&#x60; |
  | validate connections | check connection is alive before using it | user | Boolean | False | &#x60;True&#x60; |
  | port | Port | user | Integer | True | &#x60;5432&#x60; |
  | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as &#x27;schema.name&#x27; or just &#x27;name&#x27; | user | String | False | &#x60; &#x60; |
  | Support on the fly geometry simplification | When enabled, operations such as map rendering will pass a hint that will enable the usage of ST_Simplify | user | Boolean | False | &#x60;True&#x60; |
  | create database | Creates the database if it does not exist yet | advanced | Boolean | False | &#x60;False&#x60; |
  | create database params | Extra specifications appeneded to the CREATE DATABASE command | advanced | String | False | &#x60;&#x60; |
  | dbtype | Type | program | String | True | &#x60;postgis&#x60; |
  | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | &#x60;1&#x60; |
  | namespace | Namespace prefix | user | String | False | &#x60; &#x60; |
  | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | &#x60;300&#x60; |
  | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | &#x60; &#x60; |
  | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | &#x60;False&#x60; |
  | min connections | minimum number of pooled connection | user | Integer | False | &#x60;1&#x60; |
  | Max open prepared statements | Maximum number of prepared statements kept open and cached for each connection in the pool. Set to 0 to have unbounded caching, to -1 to disable caching | user | Integer | False | &#x60;50&#x60; |
  | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | &#x60; &#x60; |
  | passwd | password used to login | user | String | False | &#x60; &#x60; |
  | encode functions | set to true to have a set of filter functions be translated directly in SQL. Due to differences in the type systems the result might not be the same as evaluating them in memory, including the SQL failing with errors while the in memory version works fine. However this allows to push more of the filter into the database, increasing performance.the postgis table. | advanced | Boolean | False | &#x60;False&#x60; |
  | host | Host | user | String | True | &#x60;localhost&#x60; |
  | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | &#x60;3&#x60; |
  | Loose bbox | Perform only primary filter on bbox | user | Boolean | False | &#x60;True&#x60; |
  | Evictor run periodicity | number of seconds between idle object evitor runs (default, 300 seconds) | user | Integer | False | &#x60;300&#x60; |
  | Estimated extends | Use the spatial index information to quickly get an estimate of the data bounds | user | Boolean | False | &#x60;True&#x60; |
  | database | Database | user | String | False | &#x60; &#x60; |
  | fetch size | number of records read with each iteraction with the dbms | user | Integer | False | &#x60;1000&#x60; |
  | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | &#x60;True&#x60; |
  | max connections | maximum number of open connections | user | Integer | False | &#x60;10&#x60; |
  | preparedStatements | Use prepared statements | user | Boolean | False | &#x60;False&#x60; |
  | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | &#x60; &#x60; |
  | schema | Schema | user | String | False | &#x60;public&#x60; |
  | user | user name to login as | user | String | True | &#x60; &#x60; |

- Shapefile


  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;name&quot;: &quot;nyc&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;url&quot;,&quot;$&quot;:&quot;file:/path/to/nyc.shp&quot;}
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | &#x60;True&#x60; |
  | namespace | uri to a the namespace | advanced | URI | False | &#x60; &#x60; |
  | filetype | Discriminator for directory stores | program | String | False | &#x60;shapefile&#x60; |
  | charset | character used to decode strings from the DBF file | advanced | Charset | False | &#x60;ISO-8859-1&#x60; |
  | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | &#x60;True&#x60; |
  | fstype | Enable using a setting of &#x27;shape&#x27;. | advanced | String | False | &#x60;shape&#x60; |
  | url | url to a .shp file | user | URL | True | &#x60; &#x60; |
  | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | &#x60;True&#x60; |
  | memory mapped buffer | enable/disable the use of memory-mapped io | advanced | Boolean | False | &#x60;False&#x60; |
  | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | &#x60;Pacific Standard Time&#x60; |

- Directory of spatial files (shapefiles)


  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;name&quot;: &quot;nyc&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;url&quot;,&quot;$&quot;:&quot;file:/path/to/directory&quot;}
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | &#x60;True&#x60; |
  | namespace | uri to a the namespace | advanced | URI | False | &#x60; &#x60; |
  | filetype | Discriminator for directory stores | program | String | False | &#x60;shapefile&#x60; |
  | charset | character used to decode strings from the DBF file | advanced | Charset | False | &#x60;ISO-8859-1&#x60; |
  | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | &#x60;True&#x60; |
  | fstype | Enable using a setting of &#x27;shape&#x27;. | advanced | String | False | &#x60;shape&#x60; |
  | url | url to a .shp file | user | URL | True | &#x60; &#x60; |
  | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | &#x60;True&#x60; |
  | memory mapped buffer | enable/disable the use of memory-mapped io | advanced | Boolean | False | &#x60;False&#x60; |
  | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | &#x60;Pacific Standard Time&#x60; |


- Web Feature Service


  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;name&quot;: &quot;nyc&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;GET_CAPABILITIES_URL&quot;,&quot;$&quot;:&quot;http://localhost:8080/geoserver/wfs?request&#x3D;GetCapabilities&quot;}
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Protocol | Sets a preference for the HTTP protocol to use when requesting WFS functionality. Set this value to Boolean.TRUE for POST, Boolean.FALSE for GET or NULL for AUTO | user | Boolean | False | &#x60; &#x60; |
  | WFS GetCapabilities URL | Represents a URL to the getCapabilities document or a server instance. | user | URL | False | &#x60; &#x60; |
  | Buffer Size | This allows the user to specify a buffer size in features. This param has a default value of 10 features. | user | Integer | False | &#x60;10&#x60; |
  | Filter compliance | Level of compliance to WFS specification (0-low,1-medium,2-high) | user | Integer | False | &#x60; &#x60; |
  | EntityResolver | Sets the entity resolver used to expand XML entities | program | EntityResolver | False | &#x60;org.geotools.xml.PreventLocalEntityResolver@75e98519&#x60; |
  | Time-out | This allows the user to specify a timeout in milliseconds. This param has a default value of 3000ms. | user | Integer | False | &#x60;3000&#x60; |
  | GmlComplianceLevel | Optional OGC GML compliance level required. | user | Integer | False | &#x60;0&#x60; |
  | Lenient | Indicates that datastore should do its best to create features from the provided data even if it does not accurately match the schema.  Errors will be logged but the parsing will continue if this is true.  Default is false | user | Boolean | False | &#x60;False&#x60; |
  | Password | This allows the user to specify a username. This param should not be used without the USERNAME param. | user | String | False | &#x60; &#x60; |
  | Use Default SRS | Use always the declared DefaultSRS for requests and reproject locally if necessary | advanced | Boolean | False | &#x60;False&#x60; |
  | Namespace | Override the original WFS type name namespaces | advanced | String | False | &#x60; &#x60; |
  | Username | This allows the user to specify a username. This param should not be used without the PASSWORD param. | user | String | False | &#x60; &#x60; |
  | Axis Order Filter | Indicates axis order used by the remote WFS server for filters. It applies only to WFS 1.x.0 servers. Default is the same as AXIS_ORDER | advanced | String | False | &#x60; &#x60; |
  | GmlCompatibleTypeNames | Use Gml Compatible TypeNames (replace : by _). | user | Boolean | False | &#x60;False&#x60; |
  | Maximum features | Positive integer used as a hard limit for the amount of Features to retrieve for each FeatureType. A value of zero or not providing this parameter means no limit. | user | Integer | False | &#x60;0&#x60; |
  | Axis Order | Indicates axis order used by the remote WFS server in result coordinates. It applies only to WFS 1.x.0 servers. Default is Compliant | advanced | String | False | &#x60;Compliant&#x60; |
  | WFS Strategy | Override wfs stragegy with either cubwerx, ionic, mapserver, geoserver, strict, nonstrict or arcgis strategy. | user | String | False | &#x60;auto&#x60; |
  | Try GZIP | Indicates that datastore should use gzip to transfer data if the server supports it. Default is true | user | Boolean | False | &#x60;True&#x60; |
  | Encoding | This allows the user to specify the character encoding of the XML-Requests sent to the Server. Defaults to UTF-8 | user | String | False | &#x60;UTF-8&#x60; |
  | Outputformat | This allows the user to specify an outputFormat, different from the default one. | advanced | String | False | &#x60; &#x60; |
 | 
 **workspace_name** | **str**| The name of the worskpace containing the data stores. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datastore**
> delete_datastore(workspace_name, store_name, recurse=recurse)

Delete data store

Deletes a data store from the server.

### Example
```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.DatastoresApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the worskpace containing the data store.
store_name = 'store_name_example' # str | The name of the data store to retrieve.
recurse = true # bool | The recurse controls recursive deletion. When set to true all resources contained in the store are also removed. The default value is \"false\". (optional)

try:
    # Delete data store
    api_instance.delete_datastore(workspace_name, store_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling DatastoresApi->delete_datastore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the worskpace containing the data store. | 
 **store_name** | **str**| The name of the data store to retrieve. | 
 **recurse** | **bool**| The recurse controls recursive deletion. When set to true all resources contained in the store are also removed. The default value is \&quot;false\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_store**
> DataStoreWrapper get_data_store(workspace_name, store_name, quiet_on_not_found=quiet_on_not_found)

Retrieve a particular data store from a workspace

Controls a particular data store in a given workspace.

### Example
```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.DatastoresApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the worskpace containing the data store.
store_name = 'store_name_example' # str | The name of the data store to retrieve.
quiet_on_not_found = true # bool |  (optional) (default to true)

try:
    # Retrieve a particular data store from a workspace
    api_response = api_instance.get_data_store(workspace_name, store_name, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatastoresApi->get_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the worskpace containing the data store. | 
 **store_name** | **str**| The name of the data store to retrieve. | 
 **quiet_on_not_found** | **bool**|  | [optional] [default to true]

### Return type

[**DataStoreWrapper**](DataStoreWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datastores**
> DataStoresListResponse get_datastores(workspace_name)

Get a list of data stores

List all data stores in workspace ws.

### Example
```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.DatastoresApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the worskpace containing the data stores.

try:
    # Get a list of data stores
    api_response = api_instance.get_datastores(workspace_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatastoresApi->get_datastores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the worskpace containing the data stores. | 

### Return type

[**DataStoresListResponse**](DataStoresListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_data_store**
> modify_data_store(body, workspace_name, store_name)

Modify a data store.

Modify data store ds.

### Example
```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.DatastoresApi(geoserver.ApiClient(configuration))
body = geoserver.DataStoreInfoWrapper() # DataStoreInfoWrapper | The updated data store definition.
For a PUT, only values which should be changed need to be included. The connectionParameters map counts as a single value, 
so if you change it all preexisting connection parameters will be overwritten.

The contents of the connection parameters will differ depending on the type of data store being added.

- GeoPackage

  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "description": "A data store",
        "enabled": "true",
        "_default": "true",
        "connectionParameters": {
          "entry": [
            {"@key":"database","$":"file:///path/to/nyc.gpkg"},
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as 'schema.name' or just 'name' | user | String | False | ` ` |
  | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | ` ` |
  | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | `3` |
  | database | Database | user | File | True | ` ` |
  | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | `1` |
  | fetch size | number of records read with each iteraction with the dbms | user | Integer | False | `1000` |
  | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | `20` |
  | namespace | Namespace prefix | user | String | False | ` ` |
  | max connections | maximum number of open connections | user | Integer | False | `10` |
  | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | `True` |
  | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | `300` |
  | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | ` ` |
  | validate connections | check connection is alive before using it | user | Boolean | False | `True` |
  | dbtype | Type | program | String | True | `geopkg` |
  | passwd | password used to login | user | String | False | ` ` |
  | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | `False` |
  | min connections | minimum number of pooled connection | user | Integer | False | `1` |
  | Evictor run periodicity | number of seconds between idle object evitor runs (default, 300 seconds) | user | Integer | False | `300` |
  | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | ` ` |
  | user | user name to login as | user | String | False | ` ` |

- PostGIS

  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "description": "A data store",
        "enabled": "true",
        "_default": "true",
        "connectionParameters": {
          "entry": [
            {"@key":"host","$":"localhost"},
            {"@key":"port","$":"5432"},
            {"@key":"database","$":"nyc"},
            {"@key":"user","$":"bob"},
            {"@key":"passwd","$":"postgres"},
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | `20` |
  | validate connections | check connection is alive before using it | user | Boolean | False | `True` |
  | port | Port | user | Integer | True | `5432` |
  | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as 'schema.name' or just 'name' | user | String | False | ` ` |
  | Support on the fly geometry simplification | When enabled, operations such as map rendering will pass a hint that will enable the usage of ST_Simplify | user | Boolean | False | `True` |
  | create database | Creates the database if it does not exist yet | advanced | Boolean | False | `False` |
  | create database params | Extra specifications appeneded to the CREATE DATABASE command | advanced | String | False | `` |
  | dbtype | Type | program | String | True | `postgis` |
  | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | `1` |
  | namespace | Namespace prefix | user | String | False | ` ` |
  | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | `300` |
  | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | ` ` |
  | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | `False` |
  | min connections | minimum number of pooled connection | user | Integer | False | `1` |
  | Max open prepared statements | Maximum number of prepared statements kept open and cached for each connection in the pool. Set to 0 to have unbounded caching, to -1 to disable caching | user | Integer | False | `50` |
  | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | ` ` |
  | passwd | password used to login | user | String | False | ` ` |
  | encode functions | set to true to have a set of filter functions be translated directly in SQL. Due to differences in the type systems the result might not be the same as evaluating them in memory, including the SQL failing with errors while the in memory version works fine. However this allows to push more of the filter into the database, increasing performance.the postgis table. | advanced | Boolean | False | `False` |
  | host | Host | user | String | True | `localhost` |
  | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | `3` |
  | Loose bbox | Perform only primary filter on bbox | user | Boolean | False | `True` |
  | Evictor run periodicity | number of seconds between idle object evitor runs (default, 300 seconds) | user | Integer | False | `300` |
  | Estimated extends | Use the spatial index information to quickly get an estimate of the data bounds | user | Boolean | False | `True` |
  | database | Database | user | String | False | ` ` |
  | fetch size | number of records read with each iteraction with the dbms | user | Integer | False | `1000` |
  | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | `True` |
  | max connections | maximum number of open connections | user | Integer | False | `10` |
  | preparedStatements | Use prepared statements | user | Boolean | False | `False` |
  | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | ` ` |
  | schema | Schema | user | String | False | `public` |
  | user | user name to login as | user | String | True | ` ` |

- Shapefile

  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "description": "A data store",
        "enabled": "true",
        "_default": "true",
        "connectionParameters": {
          "entry": [
            {"@key":"url","$":"file:/path/to/nyc.shp"}
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | `True` |
  | namespace | uri to a the namespace | advanced | URI | False | ` ` |
  | filetype | Discriminator for directory stores | program | String | False | `shapefile` |
  | charset | character used to decode strings from the DBF file | advanced | Charset | False | `ISO-8859-1` |
  | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | `True` |
  | fstype | Enable using a setting of 'shape'. | advanced | String | False | `shape` |
  | url | url to a .shp file | user | URL | True | ` ` |
  | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | `True` |
  | memory mapped buffer | enable/disable the use of memory-mapped io | advanced | Boolean | False | `False` |
  | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | `Pacific Standard Time` |

- Directory of spatial files (shapefiles)

  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "description": "A data store",
        "enabled": "true",
        "_default": "true",
        "connectionParameters": {
          "entry": [
            {"@key":"url","$":"file:/path/to/directory"}
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | `True` |
  | namespace | uri to a the namespace | advanced | URI | False | ` ` |
  | filetype | Discriminator for directory stores | program | String | False | `shapefile` |
  | charset | character used to decode strings from the DBF file | advanced | Charset | False | `ISO-8859-1` |
  | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | `True` |
  | fstype | Enable using a setting of 'shape'. | advanced | String | False | `shape` |
  | url | url to a .shp file | user | URL | True | ` ` |
  | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | `True` |
  | memory mapped buffer | enable/disable the use of memory-mapped io | advanced | Boolean | False | `False` |
  | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | `Pacific Standard Time` |


- Web Feature Service

  Examples:
  - application/json:

    ```
    {
      "dataStore": {
        "description": "A data store",
        "enabled": "true",
        "_default": "true",
        "connectionParameters": {
          "entry": [
            {"@key":"GET_CAPABILITIES_URL","$":"http://localhost:8080/geoserver/wfs?request=GetCapabilities"}
          ]
        }
      }
    }
    ```

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Protocol | Sets a preference for the HTTP protocol to use when requesting WFS functionality. Set this value to Boolean.TRUE for POST, Boolean.FALSE for GET or NULL for AUTO | user | Boolean | False | ` ` |
  | WFS GetCapabilities URL | Represents a URL to the getCapabilities document or a server instance. | user | URL | False | ` ` |
  | Buffer Size | This allows the user to specify a buffer size in features. This param has a default value of 10 features. | user | Integer | False | `10` |
  | Filter compliance | Level of compliance to WFS specification (0-low,1-medium,2-high) | user | Integer | False | ` ` |
  | EntityResolver | Sets the entity resolver used to expand XML entities | program | EntityResolver | False | `org.geotools.xml.PreventLocalEntityResolver@75e98519` |
  | Time-out | This allows the user to specify a timeout in milliseconds. This param has a default value of 3000ms. | user | Integer | False | `3000` |
  | GmlComplianceLevel | Optional OGC GML compliance level required. | user | Integer | False | `0` |
  | Lenient | Indicates that datastore should do its best to create features from the provided data even if it does not accurately match the schema.  Errors will be logged but the parsing will continue if this is true.  Default is false | user | Boolean | False | `False` |
  | Password | This allows the user to specify a username. This param should not be used without the USERNAME param. | user | String | False | ` ` |
  | Use Default SRS | Use always the declared DefaultSRS for requests and reproject locally if necessary | advanced | Boolean | False | `False` |
  | Namespace | Override the original WFS type name namespaces | advanced | String | False | ` ` |
  | Username | This allows the user to specify a username. This param should not be used without the PASSWORD param. | user | String | False | ` ` |
  | Axis Order Filter | Indicates axis order used by the remote WFS server for filters. It applies only to WFS 1.x.0 servers. Default is the same as AXIS_ORDER | advanced | String | False | ` ` |
  | GmlCompatibleTypeNames | Use Gml Compatible TypeNames (replace : by _). | user | Boolean | False | `False` |
  | Maximum features | Positive integer used as a hard limit for the amount of Features to retrieve for each FeatureType. A value of zero or not providing this parameter means no limit. | user | Integer | False | `0` |
  | Axis Order | Indicates axis order used by the remote WFS server in result coordinates. It applies only to WFS 1.x.0 servers. Default is Compliant | advanced | String | False | `Compliant` |
  | WFS Strategy | Override wfs stragegy with either cubwerx, ionic, mapserver, geoserver, strict, nonstrict or arcgis strategy. | user | String | False | `auto` |
  | Try GZIP | Indicates that datastore should use gzip to transfer data if the server supports it. Default is true | user | Boolean | False | `True` |
  | Encoding | This allows the user to specify the character encoding of the XML-Requests sent to the Server. Defaults to UTF-8 | user | String | False | `UTF-8` |
  | Outputformat | This allows the user to specify an outputFormat, different from the default one. | advanced | String | False | ` ` |

workspace_name = 'workspace_name_example' # str | The name of the worskpace containing the data store.
store_name = 'store_name_example' # str | The name of the data store to retrieve.

try:
    # Modify a data store.
    api_instance.modify_data_store(body, workspace_name, store_name)
except ApiException as e:
    print("Exception when calling DatastoresApi->modify_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataStoreInfoWrapper**](DataStoreInfoWrapper.md)| The updated data store definition.
For a PUT, only values which should be changed need to be included. The connectionParameters map counts as a single value, 
so if you change it all preexisting connection parameters will be overwritten.

The contents of the connection parameters will differ depending on the type of data store being added.

- GeoPackage

  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;description&quot;: &quot;A data store&quot;,
        &quot;enabled&quot;: &quot;true&quot;,
        &quot;_default&quot;: &quot;true&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;database&quot;,&quot;$&quot;:&quot;file:///path/to/nyc.gpkg&quot;},
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as &#x27;schema.name&#x27; or just &#x27;name&#x27; | user | String | False | &#x60; &#x60; |
  | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | &#x60; &#x60; |
  | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | &#x60;3&#x60; |
  | database | Database | user | File | True | &#x60; &#x60; |
  | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | &#x60;1&#x60; |
  | fetch size | number of records read with each iteraction with the dbms | user | Integer | False | &#x60;1000&#x60; |
  | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | &#x60;20&#x60; |
  | namespace | Namespace prefix | user | String | False | &#x60; &#x60; |
  | max connections | maximum number of open connections | user | Integer | False | &#x60;10&#x60; |
  | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | &#x60;True&#x60; |
  | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | &#x60;300&#x60; |
  | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | &#x60; &#x60; |
  | validate connections | check connection is alive before using it | user | Boolean | False | &#x60;True&#x60; |
  | dbtype | Type | program | String | True | &#x60;geopkg&#x60; |
  | passwd | password used to login | user | String | False | &#x60; &#x60; |
  | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | &#x60;False&#x60; |
  | min connections | minimum number of pooled connection | user | Integer | False | &#x60;1&#x60; |
  | Evictor run periodicity | number of seconds between idle object evitor runs (default, 300 seconds) | user | Integer | False | &#x60;300&#x60; |
  | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | &#x60; &#x60; |
  | user | user name to login as | user | String | False | &#x60; &#x60; |

- PostGIS

  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;description&quot;: &quot;A data store&quot;,
        &quot;enabled&quot;: &quot;true&quot;,
        &quot;_default&quot;: &quot;true&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;host&quot;,&quot;$&quot;:&quot;localhost&quot;},
            {&quot;@key&quot;:&quot;port&quot;,&quot;$&quot;:&quot;5432&quot;},
            {&quot;@key&quot;:&quot;database&quot;,&quot;$&quot;:&quot;nyc&quot;},
            {&quot;@key&quot;:&quot;user&quot;,&quot;$&quot;:&quot;bob&quot;},
            {&quot;@key&quot;:&quot;passwd&quot;,&quot;$&quot;:&quot;postgres&quot;},
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | &#x60;20&#x60; |
  | validate connections | check connection is alive before using it | user | Boolean | False | &#x60;True&#x60; |
  | port | Port | user | Integer | True | &#x60;5432&#x60; |
  | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as &#x27;schema.name&#x27; or just &#x27;name&#x27; | user | String | False | &#x60; &#x60; |
  | Support on the fly geometry simplification | When enabled, operations such as map rendering will pass a hint that will enable the usage of ST_Simplify | user | Boolean | False | &#x60;True&#x60; |
  | create database | Creates the database if it does not exist yet | advanced | Boolean | False | &#x60;False&#x60; |
  | create database params | Extra specifications appeneded to the CREATE DATABASE command | advanced | String | False | &#x60;&#x60; |
  | dbtype | Type | program | String | True | &#x60;postgis&#x60; |
  | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | &#x60;1&#x60; |
  | namespace | Namespace prefix | user | String | False | &#x60; &#x60; |
  | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | &#x60;300&#x60; |
  | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | &#x60; &#x60; |
  | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | &#x60;False&#x60; |
  | min connections | minimum number of pooled connection | user | Integer | False | &#x60;1&#x60; |
  | Max open prepared statements | Maximum number of prepared statements kept open and cached for each connection in the pool. Set to 0 to have unbounded caching, to -1 to disable caching | user | Integer | False | &#x60;50&#x60; |
  | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | &#x60; &#x60; |
  | passwd | password used to login | user | String | False | &#x60; &#x60; |
  | encode functions | set to true to have a set of filter functions be translated directly in SQL. Due to differences in the type systems the result might not be the same as evaluating them in memory, including the SQL failing with errors while the in memory version works fine. However this allows to push more of the filter into the database, increasing performance.the postgis table. | advanced | Boolean | False | &#x60;False&#x60; |
  | host | Host | user | String | True | &#x60;localhost&#x60; |
  | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | &#x60;3&#x60; |
  | Loose bbox | Perform only primary filter on bbox | user | Boolean | False | &#x60;True&#x60; |
  | Evictor run periodicity | number of seconds between idle object evitor runs (default, 300 seconds) | user | Integer | False | &#x60;300&#x60; |
  | Estimated extends | Use the spatial index information to quickly get an estimate of the data bounds | user | Boolean | False | &#x60;True&#x60; |
  | database | Database | user | String | False | &#x60; &#x60; |
  | fetch size | number of records read with each iteraction with the dbms | user | Integer | False | &#x60;1000&#x60; |
  | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | &#x60;True&#x60; |
  | max connections | maximum number of open connections | user | Integer | False | &#x60;10&#x60; |
  | preparedStatements | Use prepared statements | user | Boolean | False | &#x60;False&#x60; |
  | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | &#x60; &#x60; |
  | schema | Schema | user | String | False | &#x60;public&#x60; |
  | user | user name to login as | user | String | True | &#x60; &#x60; |

- Shapefile

  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;description&quot;: &quot;A data store&quot;,
        &quot;enabled&quot;: &quot;true&quot;,
        &quot;_default&quot;: &quot;true&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;url&quot;,&quot;$&quot;:&quot;file:/path/to/nyc.shp&quot;}
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | &#x60;True&#x60; |
  | namespace | uri to a the namespace | advanced | URI | False | &#x60; &#x60; |
  | filetype | Discriminator for directory stores | program | String | False | &#x60;shapefile&#x60; |
  | charset | character used to decode strings from the DBF file | advanced | Charset | False | &#x60;ISO-8859-1&#x60; |
  | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | &#x60;True&#x60; |
  | fstype | Enable using a setting of &#x27;shape&#x27;. | advanced | String | False | &#x60;shape&#x60; |
  | url | url to a .shp file | user | URL | True | &#x60; &#x60; |
  | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | &#x60;True&#x60; |
  | memory mapped buffer | enable/disable the use of memory-mapped io | advanced | Boolean | False | &#x60;False&#x60; |
  | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | &#x60;Pacific Standard Time&#x60; |

- Directory of spatial files (shapefiles)

  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;description&quot;: &quot;A data store&quot;,
        &quot;enabled&quot;: &quot;true&quot;,
        &quot;_default&quot;: &quot;true&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;url&quot;,&quot;$&quot;:&quot;file:/path/to/directory&quot;}
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | &#x60;True&#x60; |
  | namespace | uri to a the namespace | advanced | URI | False | &#x60; &#x60; |
  | filetype | Discriminator for directory stores | program | String | False | &#x60;shapefile&#x60; |
  | charset | character used to decode strings from the DBF file | advanced | Charset | False | &#x60;ISO-8859-1&#x60; |
  | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | &#x60;True&#x60; |
  | fstype | Enable using a setting of &#x27;shape&#x27;. | advanced | String | False | &#x60;shape&#x60; |
  | url | url to a .shp file | user | URL | True | &#x60; &#x60; |
  | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | &#x60;True&#x60; |
  | memory mapped buffer | enable/disable the use of memory-mapped io | advanced | Boolean | False | &#x60;False&#x60; |
  | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | &#x60;Pacific Standard Time&#x60; |


- Web Feature Service

  Examples:
  - application/json:

    &#x60;&#x60;&#x60;
    {
      &quot;dataStore&quot;: {
        &quot;description&quot;: &quot;A data store&quot;,
        &quot;enabled&quot;: &quot;true&quot;,
        &quot;_default&quot;: &quot;true&quot;,
        &quot;connectionParameters&quot;: {
          &quot;entry&quot;: [
            {&quot;@key&quot;:&quot;GET_CAPABILITIES_URL&quot;,&quot;$&quot;:&quot;http://localhost:8080/geoserver/wfs?request&#x3D;GetCapabilities&quot;}
          ]
        }
      }
    }
    &#x60;&#x60;&#x60;

  Connection Parameters:

  | key | description | level | type | required | default |
  | --- | ----------- | ----- | ---- | -------- | ------- |
  | Protocol | Sets a preference for the HTTP protocol to use when requesting WFS functionality. Set this value to Boolean.TRUE for POST, Boolean.FALSE for GET or NULL for AUTO | user | Boolean | False | &#x60; &#x60; |
  | WFS GetCapabilities URL | Represents a URL to the getCapabilities document or a server instance. | user | URL | False | &#x60; &#x60; |
  | Buffer Size | This allows the user to specify a buffer size in features. This param has a default value of 10 features. | user | Integer | False | &#x60;10&#x60; |
  | Filter compliance | Level of compliance to WFS specification (0-low,1-medium,2-high) | user | Integer | False | &#x60; &#x60; |
  | EntityResolver | Sets the entity resolver used to expand XML entities | program | EntityResolver | False | &#x60;org.geotools.xml.PreventLocalEntityResolver@75e98519&#x60; |
  | Time-out | This allows the user to specify a timeout in milliseconds. This param has a default value of 3000ms. | user | Integer | False | &#x60;3000&#x60; |
  | GmlComplianceLevel | Optional OGC GML compliance level required. | user | Integer | False | &#x60;0&#x60; |
  | Lenient | Indicates that datastore should do its best to create features from the provided data even if it does not accurately match the schema.  Errors will be logged but the parsing will continue if this is true.  Default is false | user | Boolean | False | &#x60;False&#x60; |
  | Password | This allows the user to specify a username. This param should not be used without the USERNAME param. | user | String | False | &#x60; &#x60; |
  | Use Default SRS | Use always the declared DefaultSRS for requests and reproject locally if necessary | advanced | Boolean | False | &#x60;False&#x60; |
  | Namespace | Override the original WFS type name namespaces | advanced | String | False | &#x60; &#x60; |
  | Username | This allows the user to specify a username. This param should not be used without the PASSWORD param. | user | String | False | &#x60; &#x60; |
  | Axis Order Filter | Indicates axis order used by the remote WFS server for filters. It applies only to WFS 1.x.0 servers. Default is the same as AXIS_ORDER | advanced | String | False | &#x60; &#x60; |
  | GmlCompatibleTypeNames | Use Gml Compatible TypeNames (replace : by _). | user | Boolean | False | &#x60;False&#x60; |
  | Maximum features | Positive integer used as a hard limit for the amount of Features to retrieve for each FeatureType. A value of zero or not providing this parameter means no limit. | user | Integer | False | &#x60;0&#x60; |
  | Axis Order | Indicates axis order used by the remote WFS server in result coordinates. It applies only to WFS 1.x.0 servers. Default is Compliant | advanced | String | False | &#x60;Compliant&#x60; |
  | WFS Strategy | Override wfs stragegy with either cubwerx, ionic, mapserver, geoserver, strict, nonstrict or arcgis strategy. | user | String | False | &#x60;auto&#x60; |
  | Try GZIP | Indicates that datastore should use gzip to transfer data if the server supports it. Default is true | user | Boolean | False | &#x60;True&#x60; |
  | Encoding | This allows the user to specify the character encoding of the XML-Requests sent to the Server. Defaults to UTF-8 | user | String | False | &#x60;UTF-8&#x60; |
  | Outputformat | This allows the user to specify an outputFormat, different from the default one. | advanced | String | False | &#x60; &#x60; |
 | 
 **workspace_name** | **str**| The name of the worskpace containing the data store. | 
 **store_name** | **str**| The name of the data store to retrieve. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

