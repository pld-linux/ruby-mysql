%define tarname mysql-ruby
Summary:	MySQL module for Ruby
Name:		ruby-mysql
Version:	2.4.2
Release:	1
License:	public domain
Group:		Applications/Ruby
Source0:	http://www.tmtm.org/mysql/ruby/mysql-ruby-%{version}.tar.gz
URL:		http://www.tmtm.org/mysql/ruby/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ruby, mysql, mysql-devel
Requires:	ruby

%description
MySQL module for Ruby

%prep
%setup -q -n %{tarname}-%{version}

%build
ruby extconf.rb --with-mysql-dir=%{_prefix}
%{__make}

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
archdir=`ruby -r rbconfig -e 'p Config::CONFIG["archdir"]'`
install -d $RPM_BUILD_ROOT/$archdir
%{__make} archdir=$RPM_BUILD_ROOT/$archdir install
find $RPM_BUILD_ROOT%{_prefix} -type f -print | sed -e "s@^$RPM_BUILD_ROOT@@g" > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(644,root,root,755)
%doc README*
%defattr(-,root,root)
