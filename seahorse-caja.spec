Summary:	PGP encryption and signing extension for Caja
Name:		seahorse-caja
Version:	1.18.5
Release:	1
License:	GPL-2.0-or-later
Group:		Graphical desktop/Other
URL:		https://github.com/darkshram/seahorse-caja/
Source:		https://github.com/darkshram/seahorse-caja/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	pkgconfig(cryptui-0.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gck-1)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(gcr-base-3)
BuildRequires:	pkgconfig(gcr-ui-3)
BuildRequires:	pkgconfig(gpgme)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcaja-extension) >= 1.17.0
BuildRequires:	pkgconfig(libnotify)

Requires:	caja

%rename caja-extension-seahorse

%description
An extension for caja which allows encryption and decryption of
OpenPGP files using GnuPG.

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md THANKS
%{_bindir}/mate-seahorse-tool
%{_libdir}/caja/extensions-2.0/libcaja-seahorse.so
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.mate.seahorse.caja.*gschema.xml
%{_datadir}/seahorse-caja/
%{_mandir}/man1/mate-seahorse-tool.1*

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n seahorse-caja-%{version}

%build
autoreconf -fiv
%configure \
	--disable-gpg-check
# --disable-silent-rules --disable-gpg-check
%make_build

%install
%make_install

# remove static stuff
#find %{buildroot} -type f -name "*.la" -delete -print

# locales
%find_lang %{name} --with-gnome --all-name

