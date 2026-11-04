# The repository root configures the modular sources and exported target.
# Retain this entry point for consumers that add the src directory.
if(NOT TARGET ira)
  add_subdirectory("${CMAKE_CURRENT_LIST_DIR}/.." "${CMAKE_CURRENT_BINARY_DIR}/ira")
endif()
