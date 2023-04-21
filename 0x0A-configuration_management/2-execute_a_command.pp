# executes command to kill process
exec{'kill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
