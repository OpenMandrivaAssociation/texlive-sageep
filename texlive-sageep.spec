# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sageep
# catalog-date 2009-01-23 11:09:06 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-sageep
Version:	1.0
Release:	1
Summary:	Format papers for the annual meeting of EEGS
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sageep
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides formatting for papers for the annual meeting
of the Environmental and Engineering Geophysical Society (EEGS)
("Application of Geophysics to Engineering and Environmental
Problems", known as SAGEEP).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/sageep/sageep.bst
%{_texmfdistdir}/tex/latex/sageep/sageep.cls
%doc %{_texmfdistdir}/doc/latex/sageep/README
%doc %{_texmfdistdir}/doc/latex/sageep/sageep.bib
%doc %{_texmfdistdir}/doc/latex/sageep/sageep.pdf
%doc %{_texmfdistdir}/doc/latex/sageep/sageep_graphic2009.jpg
%doc %{_texmfdistdir}/doc/latex/sageep/sample.pdf
%doc %{_texmfdistdir}/doc/latex/sageep/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/sageep/Makefile
%doc %{_texmfdistdir}/source/latex/sageep/sageep.dtx
%doc %{_texmfdistdir}/source/latex/sageep/sageep.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
