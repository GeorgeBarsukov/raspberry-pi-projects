sudo nmcli connection modify "meownet" ipv4.addresses 192.168.1.100/24
sudo nmcli connection modify "meownet" ipv4.gateway 192.168.1.1
sudo nmcli connection modify "meownet" ipv4.dns "1.1.1.1 8.8.8.8"
sudo nmcli connection modify "meownet" ipv4.method manual
sudo nmcli connection up "meownet"

