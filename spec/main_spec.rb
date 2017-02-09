require 'spec_helper'

describe package('httpd') do
  it { should be_installed }
end

describe package('httpd-devel') do
  it { should be_installed }
end

describe port(80) do
  it { should be_listening }
end

describe port(443) do
  it { should be_listening }
end

describe command('curl localhost') do
  its(:exit_status) { should eq 0 }
end

describe command('curl -6 localhost') do
  its(:exit_status) { should eq 0 }
end

describe command('curl -k localhost') do
  its(:exit_status) { should eq 0 }
end

describe command('curl -6 -k localhost') do
  its(:exit_status) { should eq 0 }
end
