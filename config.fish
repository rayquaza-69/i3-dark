echo
neofetch
function ms
  sudo mount UUID=ce5f0b82-2253-405b-bb85-1d3d81c31dca /home/pvtman/homey
end

function mr
  sudo umount UUID=ce5f0b82-2253-405b-bb85-1d3d81c31dca /home/pvtman/homey
end

function swappy
  sudo swapon /dev/sda6
end

function evolve
  sudo pacman -Syy
  yay
end

function crypt-opener
  sudo cryptsetup luksOpen $argv
end

function crypt-closer
  sudo cryptsetup luksClose $argv
end

function fish_greeting
end


python3 schedule.py


