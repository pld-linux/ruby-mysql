Summary:	Pure Ruby MySQL library
Summary(pl):	Biblioteka MySQL napisana w czystym Rubym
Name:		ruby-mysql
Version:	0.2.6
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.tmtm.org/ruby/mysql/%{name}-%{version}.tar.gz
# Source0-md5:	90e139a042294ed66338f369346249f1
Source1:	setup.rb
Patch0:		%{name}-socketpath.patch
URL:		http://www.tmtm.org/ruby/mysql/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%ruby_mod_ver_requires_eq
Obsoletes:	mysql-ruby
Obsoletes:	ruby-Mysql
Conflicts:	mysql-ruby
Conflicts:	ruby-Mysql
Provides:	ruby-mysql-library
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pure Ruby MySQL library.

%description -l pl
Biblioteka MySQL napisana w czystym Rubym.

%prep
%setup -q
%patch0 -p1
cp %{SOURCE1} .
mkdir lib
mv mysql.rb lib/

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir}
ruby setup.rb setup

rdoc -o rdoc lib --inline-source
rdoc --ri lib -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_rubylibdir}/mysql.rb
%{ruby_ridir}/*
