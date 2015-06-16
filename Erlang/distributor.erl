-module(distributor).

-export([distributor/0]).

distributor() ->
	receive 
		{From, listing} ->
			{ok, Dir} = file:get_cwd(),
			Files = filelib:wildcard(Dir ++ "/*"),
			From ! {listing,Files},
			distributor();
		{From, file, File} ->
			{ok, Binary} = file:read_file(File),
			Lines = string:tokens(erlang:binary_to_list(Binary), "\n"),
			From ! {lines, Lines},
			distributor();
		{From, M} -> 
			From ! M,
			distributor()
	end.
 
