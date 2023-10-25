variable "ami_id" {
    type=string
    default = "ami-03a6eaae9938c858c"
  
}

variable "instance_type" {
    type = string
    default = "t2.micro"
  
}

variable "sg_name" {
    default = "allow-all"
  
}

variable "cidr_blocks" {
    type=list 
    default = ["0.0.0.0/0"]
  

}

variable "num" {
    type=number
    default = 10.22222
  
}

variable "a" {
    type = list(number)
    default = [ 1,2,3,4,5,6,7]


}