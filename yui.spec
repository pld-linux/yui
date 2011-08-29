Summary:	The Yahoo! User Interface Library (YUI)
Name:		yui
Version:	2.8.2
Release:	1
License:	BSD
Group:		Applications/WWW
Source0:	http://yui.zenfs.com/releases/yui2/%{name}_%{version}r1.zip
# Source0-md5:	a13570b836fb9fba5d256e094381484b
URL:		http://developer.yahoo.com/yui/
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Yahoo! User Interface (YUI) Library is a set of utilities and
controls, written in JavaScript, for building richly interactive web
applications using techniques such as DOM scripting, DHTML and AJAX.

The YUI Library also includes several core CSS resources.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/yui
cp -a build/* $RPM_BUILD_ROOT%{php_data_dir}/yui

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/yui
