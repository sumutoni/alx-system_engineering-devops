# configure ssh using puppet
file_line { 'specify host':
  ensure => 'present',
  path   => '/root/.ssh/config',
  line   => 'Host *'
}
file_line { 'password auth':
  ensure => 'present',
  path   => '/root/.ssh/config',
  line   => '\tPasswordAuthentication no'
}
file_line { 'private key file':
  ensure => 'present',
  path   => '/root/.ssh/config',
  line   => '\tIdentityFile ~/.ssh/school'
}
