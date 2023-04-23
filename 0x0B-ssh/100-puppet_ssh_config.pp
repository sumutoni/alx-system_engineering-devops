# configure ssh using puppet
$str = "Host *\n
	\t PasswordAuthentication no\n
	\t IdentityFile ~/.ssh/school"
file { '/root/.ssh/config':
  ensure  => 'present',
  content => $str
}
