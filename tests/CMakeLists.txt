enable_testing()


# basic program with f90 caller
add_executable( f90main main.f90 )
set_target_properties( f90main PROPERTIES
  Fortran_PREPROCESS ON
  Fortran_FORMAT FREE )
target_compile_options( f90main PRIVATE
  -ffree-line-length-0)
target_link_libraries( f90main PRIVATE ira )
add_test( NAME f90main COMMAND f90main )

# basic test ira match
add_executable( test_ira test_ira.f90 )
set_target_properties( test_ira PROPERTIES
  Fortran_PREPROCESS ON
  Fortran_FORMAT FREE )
target_compile_options( test_ira PRIVATE
  -ffree-line-length-0)
target_link_libraries( test_ira PRIVATE ira )
add_test( NAME test_ira COMMAND test_ira )

# basic program with C caller
add_executable( cmain main.c )
target_link_libraries( cmain PRIVATE ira )
add_test( NAME cmain COMMAND cmain )


enable_language(CXX)
add_executable( cppmain main.cpp )
target_link_libraries( cppmain PRIVATE ira )
add_test( NAME cppmain COMMAND cppmain )

# Collinear centres have no orthonormal pair. The out-of-bounds read is in
# the library, so this copy is compiled with bounds checking.
set(ira_bounds_src "")
foreach(src ${ira_src})
  list(APPEND ira_bounds_src "${CMAKE_SOURCE_DIR}/${src}")
endforeach()
add_library(ira_bounds STATIC ${ira_bounds_src})
set_target_properties(ira_bounds PROPERTIES
  Fortran_PREPROCESS ON
  Fortran_FORMAT FREE
  POSITION_INDEPENDENT_CODE ON
  Fortran_MODULE_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/ira_bounds_mods")
target_compile_options(ira_bounds PRIVATE -fcheck=bounds -ffree-line-length-0)
target_compile_definitions(ira_bounds PRIVATE
  STRVERSION="${sem_version}" DATEVERSION=${date_version})
target_include_directories(ira_bounds PUBLIC
  "${CMAKE_CURRENT_BINARY_DIR}/ira_bounds_mods"
  "${CMAKE_CURRENT_SOURCE_DIR}/../interface")
if(LAPACK_FOUND)
  target_link_libraries(ira_bounds PUBLIC ${LAPACK_LIBRARIES})
else()
  target_link_libraries(ira_bounds PUBLIC lap_local)
endif()
add_executable(collinear_basis collinear_basis.f90)
set_target_properties(collinear_basis PROPERTIES
  Fortran_PREPROCESS ON
  Fortran_FORMAT FREE)
target_compile_options(collinear_basis PRIVATE -ffree-line-length-0)
target_link_libraries(collinear_basis PRIVATE ira_bounds)
add_test(NAME collinear_basis COMMAND collinear_basis)
