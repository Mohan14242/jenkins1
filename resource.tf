resource "aws_instance" "mohan" {
    ami = var.ami_id
    instance_type = var.instance_type
    security_groups = [aws_security_group.mysg.name]

  
}
resource "aws_security_group" "mysg" {
    name=var.sg_name
    description = "allowing all the sg"

    ingress{
        description = "allwoing all "
        from_port = 443
        to_port = 443
        protocol = "tcp"
        cidr_blocks = var.cidr_blocks
    }

    egress {
        description = "only few"
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = var.cidr_blocks
    }
  
}