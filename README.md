cd state_bucket

terraform init

terraform apply

cd

terraform init

terraform apply

open custom_domain_url 

https://apia.aleksandr-kuznetsov.com/prod/


in case of redeployment, you will need to configure the ACM certificate and DNS in Netlify. since I use a subdomain of my personal site. you can bypass this option by using the route53 domain