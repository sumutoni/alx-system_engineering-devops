# configure ssh using puppet
include stdlib

file_line { 'password auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '\tPasswordAuthentication no'
}
file_line { 'private key file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '\tIdentityFile ~/.ssh/school'
}
