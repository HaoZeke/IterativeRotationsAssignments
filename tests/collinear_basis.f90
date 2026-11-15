program collinear_basis
  !! Three centres on a line have no orthonormal pair. ira_unify must
  !! report that and return. Reading coords(:, nat+1) is an abort.
  use ira_mod
  implicit none
  integer, parameter :: nat = 3
  integer :: typ(nat), cand(nat), perm(nat), ierr
  real(ira_rp) :: coords(3, nat), rot(3, 3), tr(3), hd
  integer :: i

  typ = 1
  cand = [1, 2, 3]
  coords = 0.0_ira_rp
  do i = 1, nat
    coords(1, i) = real(i - 1, ira_rp)
  end do
  call ira_unify(nat, typ, coords, cand, &
       nat, typ, coords, cand, &
       1.2_ira_rp, rot, tr, perm, hd, ierr)
  if (ierr == 0) then
    write (*, *) 'collinear centres produced a basis'
    error stop 1
  end if
end program collinear_basis
