Name:		texlive-sageep
Version:	15878
Release:	2
Summary:	Format papers for the annual meeting of EEGS
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sageep
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sageep.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
