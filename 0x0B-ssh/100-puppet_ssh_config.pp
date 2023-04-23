# configure ssh using puppet
include stdlib

file_line { 'Host':
  ensure => 'present',
  path   => '/root/.ssh/config',
  line   => 'Host *'
}
file_line { 'password auth':
  ensure => 'present',
  path   => '/root/.ssh/config',
  line   => '   PasswordAuthentication no'
}
file_line { 'private key file':
  ensure => 'present',
  path   => '/root/.ssh/config',
  line   => '   IdentityFile ~/.ssh/school'
}
