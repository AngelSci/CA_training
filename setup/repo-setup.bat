rem Configure the AWS repository used for this course.
call conda update conda -y
call anaconda config --set sites.aws.url "http://ec2-107-23-5-12.compute-1.amazonaws.com:8080/api"
call anaconda config --set default_site aws
