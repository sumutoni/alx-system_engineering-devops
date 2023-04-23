# configure ssh using puppet
$str = "Host *\n
	\t PasswordAuthentication no\n
	\t IdentityFile ~/.ssh/school"
file { '~/.ssh/config':
  ensure  => 'absent',
  content => $str
}
