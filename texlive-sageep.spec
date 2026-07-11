%global tl_name sageep
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Format papers for the annual meeting of EEGS
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sageep
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides formatting for papers for the annual meeting of the
Environmental and Engineering Geophysical Society (EEGS) ("Application
of Geophysics to Engineering and Environmental Problems", known as
SAGEEP).

