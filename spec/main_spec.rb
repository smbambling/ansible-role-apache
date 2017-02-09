require 'spec_helper'

describe package('httpd') do
  it { should be_installed }
end

describe package('httpd-devel') do
  it { should be_installed }
end
