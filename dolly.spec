%define name    dolly
%define version  0.57
%define release %mkrel 10
%define lib_name_orig lib%{name}
%define lib_major 0
%define lib_name %{lib_name_orig}%{lib_major}

Name:           %{name}
Summary:	Clone the installation of one machine to many other machines
Group:		System/Cluster
Version:        %{version}
Release:        %{release}
License:	GPL
URL:		http://www.cs.inf.ethz.ch/stricker/CoPs/patagonia/dolly.html
#Requires:
BuildRoot:      %{_tmppath}/%{name}-%{version}
Prefix:         %{_prefix}
Source:         %{name}-%{version}.tar.bz2
Source10:	dolly.html
Source11:	dolly.conf
#Patch0:

%description
Dolly is used to clone the installation of one machine to 
(possibly many) other machines. It can distribute image-files 
(even gnu-zipped), partitions or whole hard disk drives to 
other partitions or hard disk drives. As it forms a "virtual TCP 
ring" to distribute data, it works best with fast switched 
networks (we were able to clone a 2 GB Windows NT partition 
to 15 machines in our cluster over Gigabit Ethernet in less 
than 4 minutes).

As dolly clones whole partitions block-wise it works for most 
filesystems. We used it to clone partitions of the following 
type: Linux, Windows NT, Oberon, Solaris (most of our machines 
have multi boot setups). We have a small (additional) Linux 
installation on all of our machines or use a small one-floppy-disk-linux 
(e.g. muLinux) to do the cloning. 

%prep
rm -rf %{RPM_BUILD_ROOT}
%setup -q -n %{name}-%{version}
#%patch0 -p0

%build
gcc dolly.c -o dolly

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
install -m755 $RPM_BUILD_DIR/%{name}-%{version}/dolly %{buildroot}%{_bindir}/dolly
cp -v %{SOURCE10} ${RPM_BUILD_DIR}/%{name}-%{version}
cp -v %{SOURCE11} %{buildroot}%{_sysconfdir}/%{name}.conf

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc README dolly.html
%attr(755,root,root) %{_bindir}/dolly
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.57-10mdv2011.0
+ Revision: 610266
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.57-9mdv2009.0
+ Revision: 244451
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.57-7mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.57-7mdv2008.0
+ Revision: 42993
- fix group
- fix group


* Thu Mar 01 2007 aginies <aginies> 0.57-5mdv2007.0
+ Revision: 130565
- Import dolly

* Sat Jun 24 2006 Antoine Ginies <aginies@mandriva.com> 0.57-5mdv2007.0
- really add the configuration file :)
- remove unneeded provides

* Sat Jun 24 2006 Antoine Ginies <aginies@mandriva.com> 0.57-4mdv2007.0
- add a default configuration file

* Mon Mar 21 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 0.57-3mdk
- add html doc

