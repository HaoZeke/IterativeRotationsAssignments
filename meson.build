## SPDX-License-Identifier: GPL-3.0-or-later AND Apache-2.0
## Native meson build for IterativeRotationsAssignments (libira).
## Exposes ira_dep for downstream meson consumers.

project('ira', ['c', 'fortran'],
  version: '1.2.1',
  meson_version: '>= 0.60.0',
  default_options: [
    'fortran_std=none',
    'buildtype=release',
  ],
)

fc = meson.get_compiler('fortran')

lapack_dep = dependency('lapack', required: false)
if not lapack_dep.found()
  lapack_dep = dependency('lapack', method: 'cmake', required: false)
endif
if not lapack_dep.found()
  lapack_dep = fc.find_library('lapack', required: true)
endif

fortran_args = []
if fc.get_id() == 'gcc'
  fortran_args += '-ffree-line-length-none'
endif

ira_sources = files(
  'src/ira_precision.f90',
  'src/timer.f90',
  'src/sofi_tools.f90',
  'src/err_module.f90',
  'src/version.f90',
  'src/sorting_module.f90',
  'src/set_candidate.f90',
  'src/cshda.f90',
  'src/ira_routines.f90',
  'src/sofi_routines.f90',
  'src/library_ira.f90',
  'src/library_sofi.f90',
)

ira_inc = include_directories('interface')

ira_lib = library('ira',
  ira_sources,
  fortran_args: fortran_args,
  dependencies: lapack_dep,
  include_directories: ira_inc,
  install: true,
  pic: true,
)

install_headers('interface/iralib_interf.h')

ira_dep = declare_dependency(
  link_with: ira_lib,
  include_directories: ira_inc,
)

meson.override_dependency('ira', ira_dep)
