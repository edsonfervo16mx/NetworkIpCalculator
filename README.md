# Network-Ip-Calculator
 Network Ip Calculator with Python

## Getting starting
_You must have Python installed on your system._
_Clone the repository and run the main function._
### Main function
```
requestDataIp('192.168.10.10/20')
```
_Print the result in terminal._
```
print(requestDataIp('192.168.10.10/20'))
```

### Result in JSON format
```
{
   "data":[
      {
         "ip_request":"192.168.10.10",
         "cidr":"20",
         "netmask":"255.255.240.0",
         "binary_ip":"11000000101010000000101000001010",
         "ip":"192.168.10.10",
         "binary_network":"11000000101010000000000000000000",
         "ip_network":"192.168.0.0",
         "binary_first_host":"11000000101010000000000000000001",
         "ip_first_host":"192.168.0.1",
         "binary_last_host":"11000000101010000000111111111110",
         "ip_last_host":"192.168.15.254",
         "binary_broadcast":"11000000101010000000111111111111",
         "ip_broadcast":"192.168.15.255"
      }
   ]
}
```