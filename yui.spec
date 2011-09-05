Summary:	The Yahoo! User Interface Library (YUI)
Name:		yui
Version:	2.9.0
Release:	1
License:	BSD
Group:		Applications/WWW
# Source0Download: http://yuilibrary.com/download/yui2/
Source0:	http://yui.zenfs.com/releases/yui2/%{name}_%{version}.zip
# Source0-md5:	fbd1a6ae610cbf513793677a30ad1497
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
