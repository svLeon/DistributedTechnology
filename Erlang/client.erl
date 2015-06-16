-module(client).
-export([start/0, write/1]).

start() ->
	net_kernel:connect_node('distrib@localhost'),
	Pid = spawn('distrib@localhost', distributor, distributor, []),
	Pid ! {self(), listing},
	receive 
		{listing, Files} ->
			io:format('Listing : ~n',[]), write(Files)
	end,
	{ok, [NumFile]} = io:fread('input file number : ', "~d"),
	File = lists:nth(NumFile, Files),
	io:fwrite(File),
	io:fwrite('~n'),
	Pid ! {self(), file, File},
	receive 
		{lines, Lines} ->
			write(Lines)
	end.
	
write([M]) ->
	io:fwrite(M),
	io:fwrite('~n');
write([X|Y]) ->
	io:fwrite(X),
	io:fwrite('~n'),
	write(Y).