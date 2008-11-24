Summary:	The Yahoo! User Interface Library (YUI)
Name:		yui
Version:	2.6.0
Release:	0.1
License:	BSD
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/yui/%{name}_%{version}.zip
# Source0-md5:	41bed4b882c9148cebff5dd1a0dd8727
URL:		http://developer.yahoo.com/yui/
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
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
