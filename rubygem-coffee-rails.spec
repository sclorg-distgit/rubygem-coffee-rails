%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from coffee-rails-3.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coffee-rails

Summary: Coffee Script adapter for the Rails asset pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.0
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/rails/coffee-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(coffee-script) >= 2.2.0
Requires: %{?scl_prefix}rubygem(railties) => 4.0.0
Requires: %{?scl_prefix}rubygem(railties) < 5.0.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}rubygem(coffee-script) >= 2.2.0
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(railties) => 4.0.0
BuildRequires: %{?scl_prefix}rubygem(railties) < 5.0.0
BuildRequires: %{?scl_prefix}rubygem(sprockets-rails)
BuildRequires: %{?scl_prefix}rubygem(therubyracer)
%{?scl:BuildRequires: scldevel(v8)}
BuildRequires: %{?scl_prefix}rubygem(tzinfo)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Coffee Script adapter for the Rails asset pipeline.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} %{scl_v8} - << \EOF}
ruby -I.:test:lib -e 'Dir.glob("test/**/*_test.rb").each {|t| require t}'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Mon Feb 17 2014 Josef Stribny <jstribny@redhat.com> - 4.0.0-4
- Depend on scldevel(v8) virtual provide

* Thu Nov 28 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-3
- Use v8 macro

* Thu Oct 17 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-2
- Convert to scl

* Mon Aug 05 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to coffee-rails 4.0.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.2-1
- Initial package
