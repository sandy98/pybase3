<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Python: package pybase3</title>
</head><body>

<table class="heading">
<tr class="heading-text decor">
<td class="title">&nbsp;<br><strong class="title">pybase3</strong> (version 1.98.11)</td>
<td class="extra"><a href=".">index</a><br><a href="file:/home/ernesto/.local/lib/python3.11/site-packages/pybase3/__init__.py">/home/ernesto/.local/lib/python3.11/site-packages/pybase3/__init__.py</a></td></tr></table>
    <p><span class="code">pybase3<br>
&nbsp;<br>
This&nbsp;module&nbsp;provides&nbsp;a&nbsp;class&nbsp;to&nbsp;manipulate&nbsp;DBase&nbsp;III&nbsp;database&nbsp;files.<br>
It&nbsp;allows&nbsp;reading,&nbsp;writing,&nbsp;adding,&nbsp;updating&nbsp;and&nbsp;deleting&nbsp;records&nbsp;in&nbsp;the&nbsp;database.<br>
Includes&nbsp;classes&nbsp;<a href="#Connection">Connection</a>&nbsp;and&nbsp;<a href="#Cursor">Cursor</a>&nbsp;to&nbsp;interact&nbsp;with&nbsp;the&nbsp;database&nbsp;in&nbsp;a&nbsp;Python&nbsp;DB-API&nbsp;2.0&nbsp;compliant&nbsp;way.&nbsp;<br>
&nbsp;<br>
Classes:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile">DbaseFile</a>&nbsp;(Main&nbsp;class)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseHeader">DbaseHeader</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseField">DbaseField</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#Record">Record</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#FieldType">FieldType</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;SQLParser&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Additional&nbsp;class&nbsp;for&nbsp;SQL&nbsp;queries.&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It&nbsp;stands&nbsp;alone&nbsp;and&nbsp;can&nbsp;be&nbsp;used&nbsp;independently&nbsp;of&nbsp;the&nbsp;DBaseFile&nbsp;class.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It's&nbsp;used&nbsp;internally&nbsp;by&nbsp;the&nbsp;DBaseFile&nbsp;class&nbsp;to&nbsp;parse&nbsp;SQL&nbsp;queries.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Resides&nbsp;in&nbsp;its&nbsp;own&nbsp;module,&nbsp;sqlparser.py)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#Connection">Connection</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#Cursor">Cursor</a><br>
&nbsp;<br>
Functions:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#-connect">connect</a>(filename:&nbsp;str)&nbsp;-&gt;&nbsp;<a href="#Connection">Connection</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#-make_raw_lines">make_raw_lines</a>(curr:&nbsp;<a href="#Cursor">Cursor</a>)-&gt;&nbsp;Generator[str,&nbsp;None,&nbsp;None]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#-make_list_lines">make_list_lines</a>(curr:&nbsp;<a href="#Cursor">Cursor</a>)-&gt;&nbsp;Generator[str,&nbsp;None,&nbsp;None]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#-make_csv_lines">make_csv_lines</a>(curr:&nbsp;<a href="#Cursor">Cursor</a>)-&gt;&nbsp;Generator[str,&nbsp;None,&nbsp;None]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#-make_table_lines">make_table_lines</a>(curr:&nbsp;<a href="#Cursor">Cursor</a>)-&gt;Generator[str,&nbsp;None,&nbsp;None]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#-make_pretty_table_lines">make_pretty_table_lines</a>(curr:&nbsp;<a href="#Cursor">Cursor</a>)-&gt;&nbsp;Generator[str,&nbsp;None,&nbsp;None]<br>
&nbsp;<br>
CLI&nbsp;scripts:<br>
&nbsp;&nbsp;&nbsp;&nbsp;dbfview:&nbsp;(dbfview.py)&nbsp;A&nbsp;simple&nbsp;command&nbsp;line&nbsp;utility&nbsp;to&nbsp;view&nbsp;DBase&nbsp;III&nbsp;files.<br>
&nbsp;&nbsp;&nbsp;&nbsp;dbfquery:&nbsp;(dbfquery.py)&nbsp;A&nbsp;simple&nbsp;command&nbsp;line&nbsp;utility&nbsp;to&nbsp;query/update&nbsp;DBase&nbsp;III&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;files&nbsp;using&nbsp;SQL&nbsp;commands.<br>
&nbsp;&nbsp;&nbsp;&nbsp;dbfheader:&nbsp;(header_reader.py)&nbsp;A&nbsp;simple&nbsp;command&nbsp;line&nbsp;utility&nbsp;to&nbsp;read&nbsp;the&nbsp;header<br>
&nbsp;&nbsp;&nbsp;&nbsp;test:&nbsp;(test.py)&nbsp;A&nbsp;simple&nbsp;command&nbsp;line&nbsp;utility&nbsp;to&nbsp;test&nbsp;the&nbsp;library.</span></p>
<p>
<table class="section">
<tr class="decor pkg-content-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><strong class="bigsection">Package Contents</strong></td></tr>
    
<tr><td class="decor pkg-content-decor"><span class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td><td>&nbsp;</td>
<td class="singlecolumn"><table><tr><td class="multicolumn"><a href="pybase3.__main__.md">__main__</a><br>
<a href="pybase3.dbase3.md">dbase3</a><br>
<a href="pybase3.dbfquery.md">dbfquery</a><br>
</td><td class="multicolumn"><a href="pybase3.dbfview.md">dbfview</a><br>
<a href="pybase3.header_reader.md">header_reader</a><br>
<a href="pybase3.hexreader.md">hexreader</a><br>
</td><td class="multicolumn"><a href="pybase3.sqlparser.md">sqlparser</a><br>
<a href="pybase3.test.md">test</a><br>
<a href="pybase3.utils.md">utils</a><br>
</td><td class="multicolumn"></td></tr></table></td></tr></table><p>
<table class="section">
<tr class="decor index-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><strong class="bigsection">Classes</strong></td></tr>
    
<tr><td class="decor index-decor"><span class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td><td>&nbsp;</td>
<td class="singlecolumn"><dl>
<dt class="heading-text"><a href="builtins.md#object">builtins.object</a>
</dt><dd>
<dl>
<dt class="heading-text"><a href="pybase3.md#Connection">Connection</a>
</dt><dt class="heading-text"><a href="pybase3.md#Cursor">Cursor</a>
</dt><dt class="heading-text"><a href="pybase3.md#DbaseField">DbaseField</a>
</dt><dt class="heading-text"><a href="pybase3.md#DbaseFile">DbaseFile</a>
</dt><dt class="heading-text"><a href="pybase3.md#DbaseHeader">DbaseHeader</a>
</dt></dl>
</dd>
<dt class="heading-text"><a href="enum.md#Enum">enum.Enum</a>(<a href="builtins.md#object">builtins.object</a>)
</dt><dd>
<dl>
<dt class="heading-text"><a href="pybase3.md#BoxType">BoxType</a>
</dt><dt class="heading-text"><a href="pybase3.md#FieldType">FieldType</a>
</dt></dl>
</dd>
<dt class="heading-text"><a href="pybase3.utils.md#SmartDict">pybase3.utils.SmartDict</a>(<a href="builtins.md#dict">builtins.dict</a>)
</dt><dd>
<dl>
<dt class="heading-text"><a href="pybase3.md#Record">Record</a>
</dt></dl>
</dd>
</dl>
 <p>
<table class="section">
<tr class="decor title-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><a name="BoxType">class <strong>BoxType</strong></a>(<a href="enum.md#Enum">enum.Enum</a>)</td></tr>
    
<tr><td class="decor title-decor" rowspan=2><span class="code">&nbsp;&nbsp;&nbsp;</span></td>
<td class="decor title-decor" colspan=2><span class="code"><a href="#BoxType">BoxType</a>(value,&nbsp;names=None,&nbsp;*,&nbsp;module=None,&nbsp;qualname=None,&nbsp;type=None,&nbsp;start=1,&nbsp;boundary=None)<br>
&nbsp;<br>
<a href="enum.md#Enum">Enum</a>&nbsp;for&nbsp;box&nbsp;drawing&nbsp;characters.<br>&nbsp;</span></td></tr>
<tr><td>&nbsp;</td>
<td class="singlecolumn"><dl><dt>Method resolution order:</dt>
<dd><a href="pybase3.md#BoxType">BoxType</a></dd>
<dd><a href="enum.md#Enum">enum.Enum</a></dd>
<dd><a href="builtins.md#object">builtins.object</a></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>CROSS</strong> = ┼</dl>

<dl><dt><strong>DOWN_L</strong> = └</dl>

<dl><dt><strong>DOWN_R</strong> = ┘</dl>

<dl><dt><strong>HORZ</strong> = ─</dl>

<dl><dt><strong>T_DOWN</strong> = ┬</dl>

<dl><dt><strong>T_L</strong> = ├</dl>

<dl><dt><strong>T_R</strong> = ┤</dl>

<dl><dt><strong>T_UP</strong> = ┴</dl>

<dl><dt><strong>UP_L</strong> = ┌</dl>

<dl><dt><strong>UP_R</strong> = ┐</dl>

<dl><dt><strong>VERT</strong> = │</dl>

<hr>
Data descriptors inherited from <a href="enum.md#Enum">enum.Enum</a>:<br>
<dl><dt><strong>name</strong></dt>
<dd><span class="code">The&nbsp;name&nbsp;of&nbsp;the&nbsp;Enum&nbsp;member.</span></dd>
</dl>
<dl><dt><strong>value</strong></dt>
<dd><span class="code">The&nbsp;value&nbsp;of&nbsp;the&nbsp;Enum&nbsp;member.</span></dd>
</dl>
<hr>
Methods inherited from <a href="enum.md#EnumType">enum.EnumType</a>:<br>
<dl><dt><a name="BoxType-__contains__"><strong>__contains__</strong></a>(member)<span class="grey"><span class="heading-text"> from <a href="enum.md#EnumType">enum.EnumType</a></span></span></dt><dd><span class="code">Return&nbsp;True&nbsp;if&nbsp;member&nbsp;is&nbsp;a&nbsp;member&nbsp;of&nbsp;this&nbsp;enum<br>
raises&nbsp;TypeError&nbsp;if&nbsp;member&nbsp;is&nbsp;not&nbsp;an&nbsp;enum&nbsp;member<br>
&nbsp;<br>
note:&nbsp;in&nbsp;3.12&nbsp;TypeError&nbsp;will&nbsp;no&nbsp;longer&nbsp;be&nbsp;raised,&nbsp;and&nbsp;True&nbsp;will&nbsp;also&nbsp;be<br>
returned&nbsp;if&nbsp;member&nbsp;is&nbsp;the&nbsp;value&nbsp;of&nbsp;a&nbsp;member&nbsp;in&nbsp;this&nbsp;enum</span></dd></dl>

<dl><dt><a name="BoxType-__getitem__"><strong>__getitem__</strong></a>(name)<span class="grey"><span class="heading-text"> from <a href="enum.md#EnumType">enum.EnumType</a></span></span></dt><dd><span class="code">Return&nbsp;the&nbsp;member&nbsp;matching&nbsp;`name`.</span></dd></dl>

<dl><dt><a name="BoxType-__iter__"><strong>__iter__</strong></a>()<span class="grey"><span class="heading-text"> from <a href="enum.md#EnumType">enum.EnumType</a></span></span></dt><dd><span class="code">Return&nbsp;members&nbsp;in&nbsp;definition&nbsp;order.</span></dd></dl>

<dl><dt><a name="BoxType-__len__"><strong>__len__</strong></a>()<span class="grey"><span class="heading-text"> from <a href="enum.md#EnumType">enum.EnumType</a></span></span></dt><dd><span class="code">Return&nbsp;the&nbsp;number&nbsp;of&nbsp;members&nbsp;(no&nbsp;aliases)</span></dd></dl>

<hr>
Readonly properties inherited from <a href="enum.md#EnumType">enum.EnumType</a>:<br>
<dl><dt><strong>__members__</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;mapping&nbsp;of&nbsp;member&nbsp;name-&gt;value.<br>
&nbsp;<br>
This&nbsp;mapping&nbsp;lists&nbsp;all&nbsp;enum&nbsp;members,&nbsp;including&nbsp;aliases.&nbsp;Note&nbsp;that&nbsp;this<br>
is&nbsp;a&nbsp;read-only&nbsp;view&nbsp;of&nbsp;the&nbsp;internal&nbsp;mapping.</span></dd>
</dl>
</td></tr></table> <p>
<table class="section">
<tr class="decor title-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><a name="Connection">class <strong>Connection</strong></a>(<a href="builtins.md#object">builtins.object</a>)</td></tr>
    
<tr><td class="decor title-decor" rowspan=2><span class="code">&nbsp;&nbsp;&nbsp;</span></td>
<td class="decor title-decor" colspan=2><span class="code"><a href="#Connection">Connection</a>(dirname:&nbsp;str)<br>
&nbsp;<br>
<a href="#Connection">Connection</a>&nbsp;class&nbsp;for&nbsp;database&nbsp;operations.<br>
Implements&nbsp;the&nbsp;cursor()&nbsp;and&nbsp;<a href="#Connection-execute">execute</a>(sqlcmd)&nbsp;methods&nbsp;indicated&nbsp;<br>
by&nbsp;the&nbsp;Python&nbsp;DB&nbsp;API&nbsp;2.0&nbsp;specification<br>&nbsp;</span></td></tr>
<tr><td>&nbsp;</td>
<td class="singlecolumn">Methods defined here:<br>
<dl><dt><a name="Connection-Cursor"><strong>Cursor</strong></a>(self)</dt><dd><span class="code">Method&nbsp;included&nbsp;in&nbsp;order&nbsp;to&nbsp;comply&nbsp;with&nbsp;the&nbsp;Python&nbsp;DB&nbsp;API&nbsp;2.0&nbsp;specification.<br>
&nbsp;<br>
:returns:&nbsp;<a href="#Cursor">Cursor</a>&nbsp;<a href="builtins.md#object">object</a>&nbsp;for&nbsp;database&nbsp;operations.</span></dd></dl>

<dl><dt><a name="Connection-__init__"><strong>__init__</strong></a>(self, dirname: str)</dt><dd><span class="code">Initializes&nbsp;the&nbsp;<a href="#Connection">Connection</a>&nbsp;<a href="builtins.md#object">object</a>.<br>
&nbsp;<br>
:param&nbsp;dirname:&nbsp;Directory&nbsp;name&nbsp;where&nbsp;the&nbsp;database&nbsp;files&nbsp;are&nbsp;located.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Adds&nbsp;the&nbsp;non-standard&nbsp;'dirname'&nbsp;attribute&nbsp;to&nbsp;the&nbsp;<a href="#Connection">Connection</a>&nbsp;<a href="builtins.md#object">object</a>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as&nbsp;well&nbsp;as&nbsp;the&nbsp;'name'&nbsp;attribute&nbsp;with&nbsp;the&nbsp;base&nbsp;name&nbsp;of&nbsp;the&nbsp;directory,&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and&nbsp;'tablenames'&nbsp;attribute&nbsp;with&nbsp;the&nbsp;list&nbsp;of&nbsp;table&nbsp;names.</span></dd></dl>

<dl><dt><a name="Connection-execute"><strong>execute</strong></a>(self, sql: str, args=[]) -&gt; &lt;function Connection.Cursor at 0x7efc77ba2520&gt;</dt><dd><span class="code">Executes&nbsp;a&nbsp;SQL&nbsp;command&nbsp;on&nbsp;the&nbsp;database&nbsp;file&nbsp;specified&nbsp;within&nbsp;it.<br>
&nbsp;<br>
:params&nbsp;sql:&nbsp;SQL&nbsp;command&nbsp;to&nbsp;execute.<br>
:returns:&nbsp;<a href="#Cursor">Cursor</a>&nbsp;<a href="builtins.md#object">object</a>&nbsp;with&nbsp;the&nbsp;results&nbsp;of&nbsp;the&nbsp;SQL&nbsp;command.</span></dd></dl>

<hr>
Readonly properties defined here:<br>
<dl><dt><strong>filenames</strong></dt>
<dd><span class="code">Returns&nbsp;the&nbsp;list&nbsp;of&nbsp;filenames&nbsp;within&nbsp;the&nbsp;directory&nbsp;pointed&nbsp;by&nbsp;'dirname'<br>
Includes&nbsp;the&nbsp;full&nbsp;path&nbsp;of&nbsp;each,&nbsp;including&nbsp;the&nbsp;extension.</span></dd>
</dl>
<dl><dt><strong>tablenames</strong></dt>
<dd><span class="code">Returns&nbsp;the&nbsp;list&nbsp;of&nbsp;table&nbsp;names&nbsp;within&nbsp;the&nbsp;directory&nbsp;pointed&nbsp;by&nbsp;'dirname'<br>
and&nbsp;its&nbsp;subdirectories.</span></dd>
</dl>
<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><span class="code">dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><span class="code">list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</span></dd>
</dl>
</td></tr></table> <p>
<table class="section">
<tr class="decor title-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><a name="Cursor">class <strong>Cursor</strong></a>(<a href="builtins.md#object">builtins.object</a>)</td></tr>
    
<tr><td class="decor title-decor" rowspan=2><span class="code">&nbsp;&nbsp;&nbsp;</span></td>
<td class="decor title-decor" colspan=2><span class="code"><a href="#Cursor">Cursor</a>(description:&nbsp;List[Tuple[str,&nbsp;str,&nbsp;str,&nbsp;int,&nbsp;int]]&nbsp;=&nbsp;None,&nbsp;records:&nbsp;List[pybase3.<a href="#Record">Record</a>]&nbsp;=&nbsp;None,&nbsp;**kwargs)<br>
&nbsp;<br>
<a href="#Cursor">Cursor</a>&nbsp;class&nbsp;for&nbsp;database&nbsp;operations.<br>
Implements&nbsp;the&nbsp;<a href="#Cursor-fetchone">fetchone</a>(),&nbsp;<a href="#Cursor-fetchall">fetchall</a>()&nbsp;and&nbsp;<a href="#Cursor-fetchmany">fetchmany</a>()&nbsp;methods&nbsp;indicated&nbsp;by<br>
the&nbsp;Python&nbsp;DB&nbsp;API&nbsp;2.0&nbsp;specification<br>&nbsp;</span></td></tr>
<tr><td>&nbsp;</td>
<td class="singlecolumn">Methods defined here:<br>
<dl><dt><a name="Cursor-__eq__"><strong>__eq__</strong></a>(self, other)</dt><dd><span class="code">Return&nbsp;self==value.</span></dd></dl>

<dl><dt><a name="Cursor-__init__"><strong>__init__</strong></a>(self, description: List[Tuple[str, str, str, int, int]] = None, records: List[pybase3.Record] = None, **kwargs)</dt><dd><span class="code">Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(type(self))&nbsp;for&nbsp;accurate&nbsp;signature.</span></dd></dl>

<dl><dt><a name="Cursor-__repr__"><strong>__repr__</strong></a>(self)</dt><dd><span class="code">Return&nbsp;repr(self).</span></dd></dl>

<dl><dt><a name="Cursor-execute"><strong>execute</strong></a>(self, sql: str, args=[])</dt></dl>

<dl><dt><a name="Cursor-fetchall"><strong>fetchall</strong></a>(self)</dt><dd><span class="code">Returns&nbsp;all&nbsp;records&nbsp;from&nbsp;the&nbsp;cursor.</span></dd></dl>

<dl><dt><a name="Cursor-fetchmany"><strong>fetchmany</strong></a>(self, size)</dt><dd><span class="code">Returns&nbsp;the&nbsp;next&nbsp;'size'&nbsp;records&nbsp;from&nbsp;the&nbsp;cursor.</span></dd></dl>

<dl><dt><a name="Cursor-fetchone"><strong>fetchone</strong></a>(self)</dt><dd><span class="code">Returns&nbsp;the&nbsp;next&nbsp;record&nbsp;from&nbsp;the&nbsp;cursor.</span></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><span class="code">dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><span class="code">list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>__annotations__</strong> = {'description': typing.List[typing.Tuple[int, str, str, str, int, int]], 'records': typing.Generator}</dl>

<dl><dt><strong>__dataclass_fields__</strong> = {'description': Field(name='description',type=typing.List[typing...appingproxy({}),kw_only=False,_field_type=_FIELD), 'records': Field(name='records',type=typing.Generator,defau...appingproxy({}),kw_only=False,_field_type=_FIELD)}</dl>

<dl><dt><strong>__dataclass_params__</strong> = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)</dl>

<dl><dt><strong>__hash__</strong> = None</dl>

<dl><dt><strong>__match_args__</strong> = ('description', 'records')</dl>

<dl><dt><strong>records</strong> = None</dl>

</td></tr></table> <p>
<table class="section">
<tr class="decor title-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><a name="DbaseField">class <strong>DbaseField</strong></a>(<a href="builtins.md#object">builtins.object</a>)</td></tr>
    
<tr><td class="decor title-decor" rowspan=2><span class="code">&nbsp;&nbsp;&nbsp;</span></td>
<td class="decor title-decor" colspan=2><span class="code"><a href="#DbaseField">DbaseField</a>(name:&nbsp;str&nbsp;=&nbsp;'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',&nbsp;type:&nbsp;str&nbsp;=&nbsp;'C',&nbsp;address:&nbsp;int&nbsp;=&nbsp;0,&nbsp;length:&nbsp;int&nbsp;=&nbsp;0,&nbsp;decimal:&nbsp;int&nbsp;=&nbsp;0,&nbsp;reserved:&nbsp;bytes&nbsp;=&nbsp;b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')&nbsp;-&amp;gt;&nbsp;None<br>
&nbsp;<br>
Class&nbsp;to&nbsp;represent&nbsp;a&nbsp;field&nbsp;(aka&nbsp;column)&nbsp;in&nbsp;a&nbsp;DBase&nbsp;III&nbsp;database&nbsp;file.<br>&nbsp;</span></td></tr>
<tr><td>&nbsp;</td>
<td class="singlecolumn">Methods defined here:<br>
<dl><dt><a name="DbaseField-__eq__"><strong>__eq__</strong></a>(self, other)</dt><dd><span class="code">Return&nbsp;self==value.</span></dd></dl>

<dl><dt><a name="DbaseField-__init__"><strong>__init__</strong></a>(self, name: str = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', type: str = 'C', address: int = 0, length: int = 0, decimal: int = 0, reserved: bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') -&gt; None</dt><dd><span class="code">Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(<a href="#DbaseField-type">type</a>(self))&nbsp;for&nbsp;accurate&nbsp;signature.</span></dd></dl>

<dl><dt><a name="DbaseField-__post_init__"><strong>__post_init__</strong></a>(self)</dt><dd><span class="code">Validates&nbsp;the&nbsp;field&nbsp;attributes.</span></dd></dl>

<dl><dt><a name="DbaseField-__repr__"><strong>__repr__</strong></a>(self)</dt><dd><span class="code">Return&nbsp;repr(self).</span></dd></dl>

<dl><dt><a name="DbaseField-load_bytes"><strong>load_bytes</strong></a>(self, bytes)</dt><dd><span class="code">Transforms&nbsp;a&nbsp;byte&nbsp;string&nbsp;(usually&nbsp;read&nbsp;from&nbsp;disk)&nbsp;into&nbsp;a&nbsp;<a href="#DbaseField">DbaseField</a>&nbsp;<a href="builtins.md#object">object</a>.</span></dd></dl>

<dl><dt><a name="DbaseField-to_bytes"><strong>to_bytes</strong></a>(self)</dt><dd><span class="code">Transforms&nbsp;a&nbsp;<a href="#DbaseField">DbaseField</a>&nbsp;<a href="builtins.md#object">object</a>&nbsp;into&nbsp;a&nbsp;byte&nbsp;string&nbsp;(usually&nbsp;to&nbsp;write&nbsp;to&nbsp;disk).</span></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><span class="code">dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><span class="code">list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<dl><dt><strong>alias</strong></dt>
<dd><span class="code">Returns&nbsp;the&nbsp;field&nbsp;alias,&nbsp;if&nbsp;set,&nbsp;or&nbsp;the&nbsp;field&nbsp;name&nbsp;otherwise.<br>
The&nbsp;alias&nbsp;is&nbsp;used&nbsp;in&nbsp;SQL&nbsp;queries&nbsp;to&nbsp;refer&nbsp;to&nbsp;the&nbsp;field.<br>
For&nbsp;example:&nbsp;'select&nbsp;fieldname&nbsp;as&nbsp;aliasname&nbsp;from&nbsp;tablename'</span></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>__annotations__</strong> = {'address': &lt;class 'int'&gt;, 'decimal': &lt;class 'int'&gt;, 'length': &lt;class 'int'&gt;, 'name': &lt;class 'str'&gt;, 'reserved': &lt;class 'bytes'&gt;, 'type': &lt;class 'str'&gt;}</dl>

<dl><dt><strong>__dataclass_fields__</strong> = {'address': Field(name='address',type=&lt;class 'int'&gt;,default=...appingproxy({}),kw_only=False,_field_type=_FIELD), 'decimal': Field(name='decimal',type=&lt;class 'int'&gt;,default=...appingproxy({}),kw_only=False,_field_type=_FIELD), 'length': Field(name='length',type=&lt;class 'int'&gt;,default=0...appingproxy({}),kw_only=False,_field_type=_FIELD), 'name': Field(name='name',type=&lt;class 'str'&gt;,default='\x...appingproxy({}),kw_only=False,_field_type=_FIELD), 'reserved': Field(name='reserved',type=&lt;class 'bytes'&gt;,defau...appingproxy({}),kw_only=False,_field_type=_FIELD), 'type': Field(name='type',type=&lt;class 'str'&gt;,default='C'...appingproxy({}),kw_only=False,_field_type=_FIELD)}</dl>

<dl><dt><strong>__dataclass_params__</strong> = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)</dl>

<dl><dt><strong>__hash__</strong> = None</dl>

<dl><dt><strong>__match_args__</strong> = ('name', 'type', 'address', 'length', 'decimal', 'reserved')</dl>

<dl><dt><strong>address</strong> = 0</dl>

<dl><dt><strong>decimal</strong> = 0</dl>

<dl><dt><strong>length</strong> = 0</dl>

<dl><dt><strong>name</strong> = '<span class="repr">\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</span>'</dl>

<dl><dt><strong>reserved</strong> = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'</dl>

<dl><dt><strong>type</strong> = 'C'</dl>

</td></tr></table> <p>
<table class="section">
<tr class="decor title-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><a name="DbaseFile">class <strong>DbaseFile</strong></a>(<a href="builtins.md#object">builtins.object</a>)</td></tr>
    
<tr><td class="decor title-decor" rowspan=2><span class="code">&nbsp;&nbsp;&nbsp;</span></td>
<td class="decor title-decor" colspan=2><span class="code"><a href="#DbaseFile">DbaseFile</a>(filename)<br>
&nbsp;<br>
Class&nbsp;to&nbsp;manipulate&nbsp;DBase&nbsp;III&nbsp;database&nbsp;files&nbsp;(read&nbsp;and&nbsp;write).<br>
&nbsp;<br>
Methods:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-create">create</a>(filename:&nbsp;str,&nbsp;fields:&nbsp;List[Tuple[str,&nbsp;str,&nbsp;int,&nbsp;int]])&nbsp;-&gt;&nbsp;<a href="#DbaseFile">DbaseFile</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-import_from">import_from</a>(filename:str,&nbsp;tablename:str=None,&nbsp;stype:str='sqlite3',&nbsp;exportname:str=None)&nbsp;-&gt;&nbsp;<a href="#DbaseFile">DbaseFile</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-export_to">export_to</a>(desttype:str='sqlite3',&nbsp;filename:str=None)&nbsp;-&gt;&nbsp;bool<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-__init__">__init__</a>(filename:&nbsp;str)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-__del__">__del__</a>()<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-__len__">__len__</a>()&nbsp;-&gt;&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-__getitem__">__getitem__</a>(key)&nbsp;-&gt;&nbsp;<a href="#Record">Record</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-__iter__">__iter__</a>()&nbsp;-&gt;&nbsp;Generator[<a href="#Record">Record</a>,&nbsp;None,&nbsp;None]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-__str__">__str__</a>()&nbsp;-&gt;&nbsp;str<br>
&nbsp;&nbsp;&nbsp;&nbsp;_init()<br>
&nbsp;&nbsp;&nbsp;&nbsp;_load_mdx()<br>
&nbsp;&nbsp;&nbsp;&nbsp;_save_mdx()<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-schema">schema</a>()&nbsp;-&gt;&nbsp;str<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-fields_info">fields_info</a>()&nbsp;-&gt;&nbsp;str<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-field_names">field_names</a>()&nbsp;-&gt;&nbsp;List[str]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-field_alias">field_alias</a>()&nbsp;-&gt;&nbsp;List[str]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-field_types">field_types</a>()&nbsp;-&gt;&nbsp;List[str]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-field_lengths">field_lengths</a>()&nbsp;-&gt;&nbsp;List[int]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-max_field_length">max_field_length</a>(fieldname:&nbsp;str)&nbsp;-&gt;&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-max_field_lengths">max_field_lengths</a>()&nbsp;-&gt;&nbsp;List[int]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-tmax_field_lengths">tmax_field_lengths</a>()&nbsp;-&gt;&nbsp;List[int]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-commit">commit</a>(filename:str=None)&nbsp;-&gt;&nbsp;Tuple[bool,&nbsp;int]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-pack">pack</a>(filename:str=None)&nbsp;-&gt;&nbsp;Tuple[bool,&nbsp;int]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-add_record">add_record</a>(*data)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-del_record">del_record</a>(key,&nbsp;value=True)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-update_record">update_record</a>(key,&nbsp;record)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-get_record">get_record</a>(key)&nbsp;-&gt;&nbsp;<a href="#Record">Record</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-get_field">get_field</a>(fieldname)&nbsp;-&gt;&nbsp;<a href="#DbaseField">DbaseField</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-search">search</a>(fieldname,&nbsp;value,&nbsp;start=0,&nbsp;funcname="",&nbsp;compare_function=None)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<a href="#DbaseFile-update_mdx">update_mdx</a>()<br>&nbsp;</span></td></tr>
<tr><td>&nbsp;</td>
<td class="singlecolumn">Methods defined here:<br>
<dl><dt><a name="DbaseFile-__del__"><strong>__del__</strong></a>(self)</dt><dd><span class="code">Closes&nbsp;the&nbsp;database&nbsp;file&nbsp;when&nbsp;the&nbsp;instance&nbsp;is&nbsp;destroyed.</span></dd></dl>

<dl><dt><a name="DbaseFile-__getitem__"><strong>__getitem__</strong></a>(self, key)</dt><dd><span class="code">Returns&nbsp;a&nbsp;single&nbsp;record&nbsp;(dictionary&nbsp;with&nbsp;field&nbsp;names&nbsp;and&nbsp;field&nbsp;values)&nbsp;<br>
from&nbsp;the&nbsp;database&nbsp;or&nbsp;a&nbsp;list&nbsp;of&nbsp;them&nbsp;(if&nbsp;a&nbsp;slice&nbsp;is&nbsp;used).<br>
&nbsp;<br>
:param&nbsp;key:&nbsp;Index&nbsp;of&nbsp;the&nbsp;record&nbsp;to&nbsp;retrieve,&nbsp;or&nbsp;a&nbsp;slice.</span></dd></dl>

<dl><dt><a name="DbaseFile-__init__"><strong>__init__</strong></a>(self, filename)</dt><dd><span class="code">Initializes&nbsp;an&nbsp;instance&nbsp;of&nbsp;DBase3.<br>
&nbsp;<br>
:param&nbsp;filename:&nbsp;Name&nbsp;of&nbsp;the&nbsp;database&nbsp;file.</span></dd></dl>

<dl><dt><a name="DbaseFile-__iter__"><strong>__iter__</strong></a>(self)</dt><dd><span class="code">Returns&nbsp;an&nbsp;iterator&nbsp;over&nbsp;the&nbsp;records&nbsp;in&nbsp;the&nbsp;database,&nbsp;<br>
allowing&nbsp;notation&nbsp;like&nbsp;'for&nbsp;record&nbsp;in&nbsp;dbf'.</span></dd></dl>

<dl><dt><a name="DbaseFile-__len__"><strong>__len__</strong></a>(self)</dt><dd><span class="code">Returns&nbsp;the&nbsp;number&nbsp;of&nbsp;records&nbsp;in&nbsp;the&nbsp;database,&nbsp;including&nbsp;records&nbsp;marked&nbsp;to&nbsp;be&nbsp;deleted.</span></dd></dl>

<dl><dt><a name="DbaseFile-__str__"><strong>__str__</strong></a>(self)</dt><dd><span class="code">Returns&nbsp;a&nbsp;string&nbsp;with&nbsp;information&nbsp;about&nbsp;the&nbsp;database&nbsp;file.</span></dd></dl>

<dl><dt><a name="DbaseFile-add_record"><strong>add_record</strong></a>(self, *data)</dt><dd><span class="code">Adds&nbsp;a&nbsp;new&nbsp;record&nbsp;to&nbsp;the&nbsp;database.<br>
&nbsp;<br>
:param&nbsp;record_data:&nbsp;SmartDictionary&nbsp;with&nbsp;the&nbsp;new&nbsp;record's&nbsp;data.</span></dd></dl>

<dl><dt><a name="DbaseFile-as_cursor"><strong>as_cursor</strong></a>(self, records: List[pybase3.Record] = None, fields: List[pybase3.DbaseField] = None, start: int = 0, stop: int = None, step: int = 1)</dt><dd><span class="code">Returns&nbsp;a&nbsp;cursor&nbsp;<a href="builtins.md#object">object</a>&nbsp;for&nbsp;the&nbsp;database.</span></dd></dl>

<dl><dt><a name="DbaseFile-commit"><strong>commit</strong></a>(self, filename=None)</dt><dd><span class="code">Writes&nbsp;the&nbsp;database&nbsp;to&nbsp;a&nbsp;file.&nbsp;<br>
If&nbsp;no&nbsp;filename&nbsp;is&nbsp;specified,&nbsp;the&nbsp;original&nbsp;file&nbsp;is&nbsp;overwritten.<br>
Skips&nbsp;records&nbsp;marked&nbsp;as&nbsp;deleted,&nbsp;thus&nbsp;effectively&nbsp;deleting&nbsp;them,&nbsp;<br>
and&nbsp;adjusts&nbsp;the&nbsp;header&nbsp;accordingly.</span></dd></dl>

<dl><dt><a name="DbaseFile-csv"><strong>csv</strong></a>(self, start=0, stop=None, records: &lt;function DbaseFile.list at 0x7efc77ba0f40&gt; = None)</dt><dd><span class="code">Returns&nbsp;a&nbsp;generator&nbsp;of&nbsp;CSV&nbsp;strings,&nbsp;each&nbsp;one&nbsp;with&nbsp;the&nbsp;CSV&nbsp;repr&nbsp;o&nbsp;a&nbsp;record&nbsp;in&nbsp;the&nbsp;database.</span></dd></dl>

<dl><dt><a name="DbaseFile-del_mdx"><strong>del_mdx</strong></a>(self, entry: str = '*')</dt><dd><span class="code">Deletes&nbsp;the&nbsp;.pmdx&nbsp;index&nbsp;file.</span></dd></dl>

<dl><dt><a name="DbaseFile-del_record"><strong>del_record</strong></a>(self, key, value=True)</dt><dd><span class="code">Marks&nbsp;a&nbsp;record&nbsp;as&nbsp;deleted.<br>
To&nbsp;effectively&nbsp;delete&nbsp;the&nbsp;record,&nbsp;use&nbsp;the&nbsp;<a href="#DbaseFile-commit">commit</a>()&nbsp;method&nbsp;afterwards.</span></dd></dl>

<dl><dt><a name="DbaseFile-execute"><strong>execute</strong></a>(self, sql_cmd: str, args=[])</dt><dd><span class="code">Executes&nbsp;a&nbsp;SQL&nbsp;command&nbsp;on&nbsp;the&nbsp;database.<br>
&nbsp;<br>
:param&nbsp;sql_cmd:&nbsp;SQL&nbsp;command&nbsp;to&nbsp;execute<br>
:param&nbsp;args:&nbsp;List&nbsp;of&nbsp;arguments&nbsp;to&nbsp;be&nbsp;passed&nbsp;to&nbsp;the&nbsp;SQL&nbsp;command.<br>
:returns&nbsp;<a href="#Cursor">Cursor</a>&nbsp;<a href="builtins.md#object">object</a>&nbsp;with&nbsp;the&nbsp;results&nbsp;of&nbsp;the&nbsp;SQL&nbsp;command.</span></dd></dl>

<dl><dt><a name="DbaseFile-export_to"><strong>export_to</strong></a>(self, desttype: str = 'sqlite3', filename: str = None)</dt><dd><span class="code">Exports&nbsp;the&nbsp;database&nbsp;to&nbsp;a&nbsp;destination&nbsp;of&nbsp;the&nbsp;specified&nbsp;type.</span></dd></dl>

<dl><dt><a name="DbaseFile-fields_view"><strong>fields_view</strong></a>(self, start=0, stop=None, step=1, fields: List[pybase3.DbaseField] = None, records=None)</dt><dd><span class="code">Returns&nbsp;a&nbsp;generator&nbsp;yielding&nbsp;a&nbsp;record&nbsp;with&nbsp;fields&nbsp;specified&nbsp;in&nbsp;the&nbsp;fields&nbsp;dictionary.<br>
&nbsp;<br>
:param&nbsp;start:&nbsp;Index&nbsp;of&nbsp;the&nbsp;first&nbsp;record&nbsp;to&nbsp;return.<br>
:param&nbsp;stop:&nbsp;Index&nbsp;of&nbsp;the&nbsp;last&nbsp;record&nbsp;to&nbsp;return.&nbsp;len(self)&nbsp;if&nbsp;None.<br>
:param&nbsp;step:&nbsp;Step&nbsp;between&nbsp;records&nbsp;to&nbsp;return.<br>
:param&nbsp;fields:&nbsp;List&nbsp;of&nbsp;fields&nbsp;to&nbsp;include&nbsp;in&nbsp;the&nbsp;records.<br>
:param&nbsp;records:&nbsp;List&nbsp;of&nbsp;records&nbsp;to&nbsp;include&nbsp;in&nbsp;the&nbsp;view.&nbsp;If&nbsp;omitted,&nbsp;self[:]&nbsp;is&nbsp;used<br>
:returns:&nbsp;Generator&nbsp;yielding&nbsp;records&nbsp;with&nbsp;the&nbsp;specified&nbsp;fields.</span></dd></dl>

<dl><dt><a name="DbaseFile-filter"><strong>filter</strong></a>(self, fieldname, value, compare_function=None)</dt><dd><span class="code">Returns&nbsp;a&nbsp;list&nbsp;of&nbsp;records&nbsp;(dictionaries)&nbsp;that&nbsp;meet&nbsp;the&nbsp;specified&nbsp;criteria.</span></dd></dl>

<dl><dt><a name="DbaseFile-find"><strong>find</strong></a>(self, fieldname, value, start=0, compare_function=None)</dt><dd><span class="code">Wrapper&nbsp;for&nbsp;<a href="#DbaseFile-search">search</a>()&nbsp;with&nbsp;funcname="find".<br>
Returns&nbsp;the&nbsp;first&nbsp;record&nbsp;(dictionary)&nbsp;found,&nbsp;or&nbsp;None&nbsp;if&nbsp;no&nbsp;record&nbsp;meeting&nbsp;given&nbsp;criteria&nbsp;is&nbsp;found.</span></dd></dl>

<dl><dt><a name="DbaseFile-get_field"><strong>get_field</strong></a>(self, fieldname)</dt><dd><span class="code">Returns&nbsp;the&nbsp;field&nbsp;<a href="builtins.md#object">object</a>&nbsp;with&nbsp;the&nbsp;specified&nbsp;name,&nbsp;case&nbsp;sensitive.</span></dd></dl>

<dl><dt><a name="DbaseFile-get_record"><strong>get_record</strong></a>(self, key)</dt><dd><span class="code">Retrieves&nbsp;a&nbsp;record&nbsp;(dictionary&nbsp;with&nbsp;field&nbsp;names&nbsp;and&nbsp;field&nbsp;values)&nbsp;from&nbsp;the&nbsp;database.<br>
Used&nbsp;internally&nbsp;by&nbsp;the&nbsp;__getitem__&nbsp;method.</span></dd></dl>

<dl><dt><a name="DbaseFile-headers_line"><strong>headers_line</strong></a>(self, fieldsep='')</dt><dd><span class="code">Returns&nbsp;a&nbsp;string&nbsp;containing&nbsp;the&nbsp;field&nbsp;names&nbsp;right&nbsp;aligned&nbsp;to&nbsp;max&nbsp;field&nbsp;lengths.</span></dd></dl>

<dl><dt><a name="DbaseFile-index"><strong>index</strong></a>(self, fieldname, value, start=0, compare_function=None)</dt><dd><span class="code">Wrapper&nbsp;for&nbsp;<a href="#DbaseFile-search">search</a>()&nbsp;with&nbsp;funcname="index".<br>
Returns&nbsp;index&nbsp;of&nbsp;the&nbsp;first&nbsp;record&nbsp;found,&nbsp;or&nbsp;-1&nbsp;if&nbsp;no&nbsp;record&nbsp;meeting&nbsp;given&nbsp;criteria&nbsp;is&nbsp;found.</span></dd></dl>

<dl><dt><a name="DbaseFile-line"><strong>line</strong></a>(self, record, fieldsep='', names_lengths: &lt;function DbaseFile.list at 0x7efc77ba0f40&gt; = None)</dt><dd><span class="code">Returns&nbsp;a&nbsp;string&nbsp;with&nbsp;the&nbsp;record&nbsp;at&nbsp;the&nbsp;specified&nbsp;index,&nbsp;with&nbsp;fields&nbsp;right&nbsp;aligned&nbsp;to&nbsp;max&nbsp;field&nbsp;lengths.</span></dd></dl>

<dl><dt><a name="DbaseFile-lines"><strong>lines</strong></a>(self, start=0, stop=None, fieldsep='', records: &lt;function DbaseFile.list at 0x7efc77ba0f40&gt; = None)</dt><dd><span class="code">Returns&nbsp;a&nbsp;generator&nbsp;which&nbsp;resolves&nbsp;to&nbsp;an&nbsp;array&nbsp;of&nbsp;strings,&nbsp;each&nbsp;one&nbsp;with&nbsp;<br>
with&nbsp;the&nbsp;records&nbsp;in&nbsp;the&nbsp;specified&nbsp;range,&nbsp;with&nbsp;fields&nbsp;right&nbsp;aligned&nbsp;to&nbsp;max&nbsp;field&nbsp;lengths.</span></dd></dl>

<dl><dt><a name="DbaseFile-list"><strong>list</strong></a>(self, start=0, stop=None, fieldsep='|', records: list = None)</dt><dd><span class="code">Returns&nbsp;a&nbsp;generator,&nbsp;corresponding&nbsp;to&nbsp;the&nbsp;list&nbsp;of&nbsp;records&nbsp;from&nbsp;the&nbsp;database.</span></dd></dl>

<dl><dt><a name="DbaseFile-make_mdx"><strong>make_mdx</strong></a>(self, fieldname: str = '*')</dt><dd><span class="code">Generates&nbsp;a&nbsp;.pmdx&nbsp;index&nbsp;for&nbsp;the&nbsp;specified&nbsp;field.<br>
&nbsp;<br>
:param&nbsp;fieldname:&nbsp;Name&nbsp;of&nbsp;the&nbsp;field&nbsp;to&nbsp;index.&nbsp;If&nbsp;'*',&nbsp;indexes&nbsp;all&nbsp;fields.</span></dd></dl>

<dl><dt><a name="DbaseFile-max_field_length"><strong>max_field_length</strong></a>(self, fieldname)</dt><dd><span class="code">Returns&nbsp;the&nbsp;maximum&nbsp;length&nbsp;of&nbsp;the&nbsp;specified&nbsp;field&nbsp;(including&nbsp;length&nbsp;of&nbsp;field&nbsp;name)&nbsp;in&nbsp;the&nbsp;database.</span></dd></dl>

<dl><dt><a name="DbaseFile-pack"><strong>pack</strong></a>(self, filename=None)</dt><dd><span class="code">Same&nbsp;as&nbsp;<a href="#DbaseFile-commit">commit</a>().&nbsp;Included&nbsp;for&nbsp;compatibility&nbsp;with&nbsp;long&nbsp;lost&nbsp;dBase&nbsp;past.</span></dd></dl>

<dl><dt><a name="DbaseFile-parse_conditions"><strong>parse_conditions</strong></a>(self, wherestr: str) -&gt; List[Tuple[str, Any, Callable]]</dt><dd><span class="code">Parses&nbsp;the&nbsp;WHERE&nbsp;clause&nbsp;of&nbsp;a&nbsp;SQL&nbsp;statement&nbsp;and&nbsp;returns&nbsp;a&nbsp;list&nbsp;of&nbsp;tuples<br>
with&nbsp;the&nbsp;field&nbsp;name,&nbsp;the&nbsp;value&nbsp;to&nbsp;compare&nbsp;and&nbsp;the&nbsp;comparison&nbsp;function.</span></dd></dl>

<dl><dt><a name="DbaseFile-pretty_table"><strong>pretty_table</strong></a>(self, start=0, stop=None, records: &lt;function DbaseFile.list at 0x7efc77ba0f40&gt; = None) -&gt; Generator[str, NoneType, NoneType]</dt><dd><span class="code">Returns&nbsp;a&nbsp;&nbsp;generator&nbsp;yielding&nbsp;a&nbsp;string&nbsp;for&nbsp;each&nbsp;line&nbsp;representing&nbsp;a&nbsp;record&nbsp;in&nbsp;the&nbsp;database,&nbsp;<br>
wrapped&nbsp;in&nbsp;cute&nbsp;lines.</span></dd></dl>

<dl><dt><a name="DbaseFile-save_record"><strong>save_record</strong></a>(self, key, record)</dt><dd><span class="code">Writes&nbsp;a&nbsp;record&nbsp;(dictionary&nbsp;with&nbsp;field&nbsp;names&nbsp;and&nbsp;field&nbsp;values)&nbsp;to&nbsp;the&nbsp;database<br>
at&nbsp;the&nbsp;specified&nbsp;index.</span></dd></dl>

<dl><dt><a name="DbaseFile-search"><strong>search</strong></a>(self, fieldname, value, start=0, funcname='', compare_function=None)</dt><dd><span class="code">Searches&nbsp;for&nbsp;a&nbsp;record&nbsp;with&nbsp;the&nbsp;specified&nbsp;value&nbsp;in&nbsp;the&nbsp;specified&nbsp;field,<br>
starting&nbsp;from&nbsp;the&nbsp;specified&nbsp;index,&nbsp;for&nbsp;which&nbsp;the&nbsp;specified&nbsp;comparison&nbsp;function&nbsp;returns&nbsp;True.<br>
It&nbsp;will&nbsp;try&nbsp;to&nbsp;use&nbsp;the&nbsp;field&nbsp;index&nbsp;if&nbsp;available.</span></dd></dl>

<dl><dt><a name="DbaseFile-table"><strong>table</strong></a>(self, start=0, stop=None, records: &lt;function DbaseFile.list at 0x7efc77ba0f40&gt; = None)</dt><dd><span class="code">Returns&nbsp;a&nbsp;&nbsp;generator&nbsp;yielding&nbsp;a&nbsp;string&nbsp;for&nbsp;each&nbsp;line&nbsp;representing&nbsp;a&nbsp;record&nbsp;in&nbsp;the&nbsp;database,&nbsp;<br>
wrapped&nbsp;in&nbsp;sqlite3&nbsp;style&nbsp;(.mode&nbsp;table)&nbsp;lines.</span></dd></dl>

<dl><dt><a name="DbaseFile-transform"><strong>transform</strong></a>(self, record: pybase3.Record, fields: List[pybase3.DbaseField])</dt><dd><span class="code">Returns&nbsp;a&nbsp;record&nbsp;with&nbsp;the&nbsp;specified&nbsp;fields,&nbsp;usually&nbsp;with<br>
fields&nbsp;'deleted'&nbsp;and&nbsp;'metadata'&nbsp;stripped.</span></dd></dl>

<dl><dt><a name="DbaseFile-update_mdx"><strong>update_mdx</strong></a>(self)</dt><dd><span class="code">Updates&nbsp;the&nbsp;.pmdx&nbsp;index&nbsp;file.</span></dd></dl>

<dl><dt><a name="DbaseFile-update_record"><strong>update_record</strong></a>(self, key, record)</dt><dd><span class="code">Updates&nbsp;an&nbsp;existing&nbsp;record&nbsp;in&nbsp;the&nbsp;database.<br>
&nbsp;<br>
:param&nbsp;index:&nbsp;Index&nbsp;of&nbsp;the&nbsp;record&nbsp;to&nbsp;update.<br>
:param&nbsp;record_data:&nbsp;SmartDictionary&nbsp;with&nbsp;the&nbsp;updated&nbsp;data.<br>
:raises&nbsp;IndexError:&nbsp;If&nbsp;the&nbsp;record&nbsp;index&nbsp;is&nbsp;out&nbsp;of&nbsp;range.</span></dd></dl>

<hr>
Class methods defined here:<br>
<dl><dt><a name="DbaseFile-create"><strong>create</strong></a>(filename: str, fields: List[Tuple[str, str, int, int]])<span class="grey"><span class="heading-text"> from <a href="builtins.md#type">builtins.type</a></span></span></dt><dd><span class="code">Creates&nbsp;a&nbsp;new&nbsp;DBase&nbsp;III&nbsp;database&nbsp;file&nbsp;with&nbsp;the&nbsp;specified&nbsp;fields.<br>
&nbsp;<br>
:param&nbsp;filename:&nbsp;Name&nbsp;of&nbsp;the&nbsp;file&nbsp;to&nbsp;create.<br>
:param&nbsp;fields:&nbsp;List&nbsp;of&nbsp;tuples&nbsp;describing&nbsp;the&nbsp;fields&nbsp;(name,&nbsp;type,&nbsp;length,&nbsp;decimals).<br>
:raises&nbsp;FileExistsError:&nbsp;If&nbsp;the&nbsp;file&nbsp;already&nbsp;exists.</span></dd></dl>

<dl><dt><a name="DbaseFile-import_from"><strong>import_from</strong></a>(filename: str, tablename: str = None, stype: str = 'sqlite3', exportname: str = None)<span class="grey"><span class="heading-text"> from <a href="builtins.md#type">builtins.type</a></span></span></dt><dd><span class="code">Imports&nbsp;a&nbsp;database&nbsp;from&nbsp;a&nbsp;source&nbsp;of&nbsp;the&nbsp;specified&nbsp;type.</span></dd></dl>

<hr>
Static methods defined here:<br>
<dl><dt><a name="DbaseFile-iendswith"><strong>iendswith</strong></a>(f: str, v: str) -&gt; bool</dt><dd><span class="code">Checks&nbsp;if&nbsp;the&nbsp;string&nbsp;'f'&nbsp;ends&nbsp;with&nbsp;the&nbsp;string&nbsp;'v',&nbsp;ignoring&nbsp;case.<br>
&nbsp;<br>
:param&nbsp;f:&nbsp;String&nbsp;to&nbsp;check.<br>
:param&nbsp;v:&nbsp;Suffix&nbsp;to&nbsp;look&nbsp;for.<br>
:return:&nbsp;True&nbsp;if&nbsp;'f'&nbsp;ends&nbsp;with&nbsp;'v',&nbsp;False&nbsp;otherwise.</span></dd></dl>

<dl><dt><a name="DbaseFile-istartswith"><strong>istartswith</strong></a>(f: str, v: str) -&gt; bool</dt><dd><span class="code">Checks&nbsp;if&nbsp;the&nbsp;string&nbsp;'f'&nbsp;starts&nbsp;with&nbsp;the&nbsp;string&nbsp;'v',&nbsp;ignoring&nbsp;case.<br>
&nbsp;<br>
:param&nbsp;f:&nbsp;String&nbsp;to&nbsp;check.<br>
:param&nbsp;v:&nbsp;Prefix&nbsp;to&nbsp;look&nbsp;for.<br>
:return:&nbsp;True&nbsp;if&nbsp;'f'&nbsp;starts&nbsp;with&nbsp;'v',&nbsp;False&nbsp;otherwise.</span></dd></dl>

<hr>
Readonly properties defined here:<br>
<dl><dt><strong>csv_headers_line</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;CSV&nbsp;string&nbsp;with&nbsp;the&nbsp;field&nbsp;names.</span></dd>
</dl>
<dl><dt><strong>field_alias</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;list&nbsp;with&nbsp;the&nbsp;name&nbsp;of&nbsp;each&nbsp;field&nbsp;in&nbsp;the&nbsp;database.</span></dd>
</dl>
<dl><dt><strong>field_lengths</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;list&nbsp;with&nbsp;the&nbsp;length&nbsp;of&nbsp;each&nbsp;field&nbsp;in&nbsp;the&nbsp;database.</span></dd>
</dl>
<dl><dt><strong>field_names</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;list&nbsp;with&nbsp;the&nbsp;name&nbsp;of&nbsp;each&nbsp;field&nbsp;in&nbsp;the&nbsp;database.</span></dd>
</dl>
<dl><dt><strong>field_types</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;list&nbsp;with&nbsp;the&nbsp;type&nbsp;of&nbsp;each&nbsp;field&nbsp;in&nbsp;the&nbsp;database.</span></dd>
</dl>
<dl><dt><strong>fields_info</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;string&nbsp;with&nbsp;information&nbsp;about&nbsp;the&nbsp;fields&nbsp;in&nbsp;the&nbsp;database.</span></dd>
</dl>
<dl><dt><strong>max_field_lengths</strong></dt>
<dd><span class="code">Returns&nbsp;the&nbsp;maximum&nbsp;length&nbsp;of&nbsp;each&nbsp;field&nbsp;(including&nbsp;length&nbsp;of&nbsp;field&nbsp;name)&nbsp;in&nbsp;the&nbsp;database.</span></dd>
</dl>
<dl><dt><strong>schema</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;string&nbsp;with&nbsp;the&nbsp;schema&nbsp;of&nbsp;the&nbsp;database.</span></dd>
</dl>
<dl><dt><strong>tmax_field_lengths</strong></dt>
<dd><span class="code">Returns&nbsp;the&nbsp;maximum&nbsp;length&nbsp;of&nbsp;each&nbsp;field&nbsp;(including&nbsp;length&nbsp;of&nbsp;field&nbsp;name)&nbsp;in&nbsp;the&nbsp;database.<br>
Threaded&nbsp;version.</span></dd>
</dl>
<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><span class="code">dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><span class="code">list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>export_types</strong> = ['sqlite3', 'sqlite', 'csv']</dl>

<dl><dt><strong>import_types</strong> = ['sqlite3', 'sqlite', 'csv']</dl>

</td></tr></table> <p>
<table class="section">
<tr class="decor title-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><a name="DbaseHeader">class <strong>DbaseHeader</strong></a>(<a href="builtins.md#object">builtins.object</a>)</td></tr>
    
<tr><td class="decor title-decor" rowspan=2><span class="code">&nbsp;&nbsp;&nbsp;</span></td>
<td class="decor title-decor" colspan=2><span class="code"><a href="#DbaseHeader">DbaseHeader</a>(version:&nbsp;int&nbsp;=&nbsp;3,&nbsp;year:&nbsp;int&nbsp;=&nbsp;25,&nbsp;month:&nbsp;int&nbsp;=&nbsp;1,&nbsp;day:&nbsp;int&nbsp;=&nbsp;27,&nbsp;records:&nbsp;int&nbsp;=&nbsp;0,&nbsp;header_size:&nbsp;int&nbsp;=&nbsp;0,&nbsp;record_size:&nbsp;int&nbsp;=&nbsp;0,&nbsp;reserved:&nbsp;bytes&nbsp;=&nbsp;b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')&nbsp;-&amp;gt;&nbsp;None<br>
&nbsp;<br>
Class&nbsp;to&nbsp;represent&nbsp;the&nbsp;header&nbsp;of&nbsp;a&nbsp;DBase&nbsp;III&nbsp;database&nbsp;file.<br>&nbsp;</span></td></tr>
<tr><td>&nbsp;</td>
<td class="singlecolumn">Methods defined here:<br>
<dl><dt><a name="DbaseHeader-__eq__"><strong>__eq__</strong></a>(self, other)</dt><dd><span class="code">Return&nbsp;self==value.</span></dd></dl>

<dl><dt><a name="DbaseHeader-__init__"><strong>__init__</strong></a>(self, version: int = 3, year: int = 25, month: int = 1, day: int = 27, records: int = 0, header_size: int = 0, record_size: int = 0, reserved: bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') -&gt; None</dt><dd><span class="code">Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(type(self))&nbsp;for&nbsp;accurate&nbsp;signature.</span></dd></dl>

<dl><dt><a name="DbaseHeader-__post_init__"><strong>__post_init__</strong></a>(self)</dt><dd><span class="code">Validates&nbsp;the&nbsp;header&nbsp;fields.</span></dd></dl>

<dl><dt><a name="DbaseHeader-__repr__"><strong>__repr__</strong></a>(self)</dt><dd><span class="code">Return&nbsp;repr(self).</span></dd></dl>

<dl><dt><a name="DbaseHeader-load_bytes"><strong>load_bytes</strong></a>(self, bytes)</dt><dd><span class="code">Transforms&nbsp;a&nbsp;byte&nbsp;string&nbsp;(usually&nbsp;read&nbsp;from&nbsp;disk)&nbsp;into&nbsp;a&nbsp;<a href="#DbaseHeader">DbaseHeader</a>&nbsp;<a href="builtins.md#object">object</a>.</span></dd></dl>

<dl><dt><a name="DbaseHeader-to_bytes"><strong>to_bytes</strong></a>(self)</dt><dd><span class="code">Transforms&nbsp;a&nbsp;<a href="#DbaseHeader">DbaseHeader</a>&nbsp;<a href="builtins.md#object">object</a>&nbsp;into&nbsp;a&nbsp;byte&nbsp;string&nbsp;(usually&nbsp;to&nbsp;write&nbsp;to&nbsp;disk).</span></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><span class="code">dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><span class="code">list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>__annotations__</strong> = {'day': &lt;class 'int'&gt;, 'header_size': &lt;class 'int'&gt;, 'month': &lt;class 'int'&gt;, 'record_size': &lt;class 'int'&gt;, 'records': &lt;class 'int'&gt;, 'reserved': &lt;class 'bytes'&gt;, 'version': &lt;class 'int'&gt;, 'year': &lt;class 'int'&gt;}</dl>

<dl><dt><strong>__dataclass_fields__</strong> = {'day': Field(name='day',type=&lt;class 'int'&gt;,default=27,d...appingproxy({}),kw_only=False,_field_type=_FIELD), 'header_size': Field(name='header_size',type=&lt;class 'int'&gt;,defa...appingproxy({}),kw_only=False,_field_type=_FIELD), 'month': Field(name='month',type=&lt;class 'int'&gt;,default=1,...appingproxy({}),kw_only=False,_field_type=_FIELD), 'record_size': Field(name='record_size',type=&lt;class 'int'&gt;,defa...appingproxy({}),kw_only=False,_field_type=_FIELD), 'records': Field(name='records',type=&lt;class 'int'&gt;,default=...appingproxy({}),kw_only=False,_field_type=_FIELD), 'reserved': Field(name='reserved',type=&lt;class 'bytes'&gt;,defau...appingproxy({}),kw_only=False,_field_type=_FIELD), 'version': Field(name='version',type=&lt;class 'int'&gt;,default=...appingproxy({}),kw_only=False,_field_type=_FIELD), 'year': Field(name='year',type=&lt;class 'int'&gt;,default=25,...appingproxy({}),kw_only=False,_field_type=_FIELD)}</dl>

<dl><dt><strong>__dataclass_params__</strong> = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)</dl>

<dl><dt><strong>__hash__</strong> = None</dl>

<dl><dt><strong>__match_args__</strong> = ('version', 'year', 'month', 'day', 'records', 'header_size', 'record_size', 'reserved')</dl>

<dl><dt><strong>day</strong> = 27</dl>

<dl><dt><strong>header_size</strong> = 0</dl>

<dl><dt><strong>month</strong> = 1</dl>

<dl><dt><strong>record_size</strong> = 0</dl>

<dl><dt><strong>records</strong> = 0</dl>

<dl><dt><strong>reserved</strong> = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'</dl>

<dl><dt><strong>version</strong> = 3</dl>

<dl><dt><strong>year</strong> = 25</dl>

</td></tr></table> <p>
<table class="section">
<tr class="decor title-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><a name="FieldType">class <strong>FieldType</strong></a>(<a href="enum.md#Enum">enum.Enum</a>)</td></tr>
    
<tr><td class="decor title-decor" rowspan=2><span class="code">&nbsp;&nbsp;&nbsp;</span></td>
<td class="decor title-decor" colspan=2><span class="code"><a href="#FieldType">FieldType</a>(value,&nbsp;names=None,&nbsp;*,&nbsp;module=None,&nbsp;qualname=None,&nbsp;type=None,&nbsp;start=1,&nbsp;boundary=None)<br>
&nbsp;<br>
<a href="enum.md#Enum">Enum</a>&nbsp;for&nbsp;dBase&nbsp;III&nbsp;field&nbsp;types.<br>&nbsp;</span></td></tr>
<tr><td>&nbsp;</td>
<td class="singlecolumn"><dl><dt>Method resolution order:</dt>
<dd><a href="pybase3.md#FieldType">FieldType</a></dd>
<dd><a href="enum.md#Enum">enum.Enum</a></dd>
<dd><a href="builtins.md#object">builtins.object</a></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>CHARACTER</strong> = C</dl>

<dl><dt><strong>DATE</strong> = D</dl>

<dl><dt><strong>FLOAT</strong> = F</dl>

<dl><dt><strong>LOGICAL</strong> = L</dl>

<dl><dt><strong>MEMO</strong> = M</dl>

<dl><dt><strong>NUMERIC</strong> = N</dl>

<hr>
Data descriptors inherited from <a href="enum.md#Enum">enum.Enum</a>:<br>
<dl><dt><strong>name</strong></dt>
<dd><span class="code">The&nbsp;name&nbsp;of&nbsp;the&nbsp;Enum&nbsp;member.</span></dd>
</dl>
<dl><dt><strong>value</strong></dt>
<dd><span class="code">The&nbsp;value&nbsp;of&nbsp;the&nbsp;Enum&nbsp;member.</span></dd>
</dl>
<hr>
Methods inherited from <a href="enum.md#EnumType">enum.EnumType</a>:<br>
<dl><dt><a name="FieldType-__contains__"><strong>__contains__</strong></a>(member)<span class="grey"><span class="heading-text"> from <a href="enum.md#EnumType">enum.EnumType</a></span></span></dt><dd><span class="code">Return&nbsp;True&nbsp;if&nbsp;member&nbsp;is&nbsp;a&nbsp;member&nbsp;of&nbsp;this&nbsp;enum<br>
raises&nbsp;TypeError&nbsp;if&nbsp;member&nbsp;is&nbsp;not&nbsp;an&nbsp;enum&nbsp;member<br>
&nbsp;<br>
note:&nbsp;in&nbsp;3.12&nbsp;TypeError&nbsp;will&nbsp;no&nbsp;longer&nbsp;be&nbsp;raised,&nbsp;and&nbsp;True&nbsp;will&nbsp;also&nbsp;be<br>
returned&nbsp;if&nbsp;member&nbsp;is&nbsp;the&nbsp;value&nbsp;of&nbsp;a&nbsp;member&nbsp;in&nbsp;this&nbsp;enum</span></dd></dl>

<dl><dt><a name="FieldType-__getitem__"><strong>__getitem__</strong></a>(name)<span class="grey"><span class="heading-text"> from <a href="enum.md#EnumType">enum.EnumType</a></span></span></dt><dd><span class="code">Return&nbsp;the&nbsp;member&nbsp;matching&nbsp;`name`.</span></dd></dl>

<dl><dt><a name="FieldType-__iter__"><strong>__iter__</strong></a>()<span class="grey"><span class="heading-text"> from <a href="enum.md#EnumType">enum.EnumType</a></span></span></dt><dd><span class="code">Return&nbsp;members&nbsp;in&nbsp;definition&nbsp;order.</span></dd></dl>

<dl><dt><a name="FieldType-__len__"><strong>__len__</strong></a>()<span class="grey"><span class="heading-text"> from <a href="enum.md#EnumType">enum.EnumType</a></span></span></dt><dd><span class="code">Return&nbsp;the&nbsp;number&nbsp;of&nbsp;members&nbsp;(no&nbsp;aliases)</span></dd></dl>

<hr>
Readonly properties inherited from <a href="enum.md#EnumType">enum.EnumType</a>:<br>
<dl><dt><strong>__members__</strong></dt>
<dd><span class="code">Returns&nbsp;a&nbsp;mapping&nbsp;of&nbsp;member&nbsp;name-&gt;value.<br>
&nbsp;<br>
This&nbsp;mapping&nbsp;lists&nbsp;all&nbsp;enum&nbsp;members,&nbsp;including&nbsp;aliases.&nbsp;Note&nbsp;that&nbsp;this<br>
is&nbsp;a&nbsp;read-only&nbsp;view&nbsp;of&nbsp;the&nbsp;internal&nbsp;mapping.</span></dd>
</dl>
</td></tr></table> <p>
<table class="section">
<tr class="decor title-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><a name="Record">class <strong>Record</strong></a>(<a href="pybase3.utils.md#SmartDict">pybase3.utils.SmartDict</a>)</td></tr>
    
<tr><td class="decor title-decor" rowspan=2><span class="code">&nbsp;&nbsp;&nbsp;</span></td>
<td class="decor title-decor" colspan=2><span class="code"><a href="#Record">Record</a>(*args,&nbsp;**kwargs)<br>
&nbsp;<br>
Class&nbsp;to&nbsp;represent&nbsp;a&nbsp;record&nbsp;in&nbsp;a&nbsp;DBase&nbsp;III&nbsp;database.<br>
Inherits&nbsp;from&nbsp;<a href="pybase3.utils.md#SmartDict">SmartDict</a>,&nbsp;a&nbsp;dictionary&nbsp;with&nbsp;dot&nbsp;notation&nbsp;access&nbsp;to&nbsp;keys.<br>&nbsp;</span></td></tr>
<tr><td>&nbsp;</td>
<td class="singlecolumn"><dl><dt>Method resolution order:</dt>
<dd><a href="pybase3.md#Record">Record</a></dd>
<dd><a href="pybase3.utils.md#SmartDict">pybase3.utils.SmartDict</a></dd>
<dd><a href="builtins.md#dict">builtins.dict</a></dd>
<dd><a href="builtins.md#object">builtins.object</a></dd>
</dl>
<hr>
Methods defined here:<br>
<dl><dt><a name="Record-__init__"><strong>__init__</strong></a>(self, *args, **kwargs)</dt><dd><span class="code">Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(type(self))&nbsp;for&nbsp;accurate&nbsp;signature.</span></dd></dl>

<dl><dt><a name="Record-__repr__"><strong>__repr__</strong></a>(self)</dt><dd><span class="code">Return&nbsp;repr(self).</span></dd></dl>

<dl><dt><a name="Record-__str__"><strong>__str__</strong></a>(self)</dt><dd><span class="code">Return&nbsp;str(self).</span></dd></dl>

<hr>
Readonly properties defined here:<br>
<dl><dt><strong>datafields</strong></dt>
</dl>
<dl><dt><strong>to_datafields</strong></dt>
</dl>
<hr>
Methods inherited from <a href="pybase3.utils.md#SmartDict">pybase3.utils.SmartDict</a>:<br>
<dl><dt><a name="Record-__delattr__"><strong>__delattr__</strong></a>(self, attr)</dt><dd><span class="code">Implement&nbsp;delattr(self,&nbsp;name).</span></dd></dl>

<dl><dt><a name="Record-__getattr__"><strong>__getattr__</strong></a>(self, attr)</dt></dl>

<dl><dt><a name="Record-__hasattr__"><strong>__hasattr__</strong></a>(self, attr)</dt></dl>

<dl><dt><a name="Record-__setattr__"><strong>__setattr__</strong></a>(self, attr, value)</dt><dd><span class="code">Implement&nbsp;setattr(self,&nbsp;name,&nbsp;value).</span></dd></dl>

<dl><dt><a name="Record-copy"><strong>copy</strong></a>(self)</dt><dd><span class="code">D.<a href="#Record-copy">copy</a>()&nbsp;-&gt;&nbsp;a&nbsp;shallow&nbsp;copy&nbsp;of&nbsp;D</span></dd></dl>

<hr>
Readonly properties inherited from <a href="pybase3.utils.md#SmartDict">pybase3.utils.SmartDict</a>:<br>
<dl><dt><strong>parent</strong></dt>
</dl>
<hr>
Data descriptors inherited from <a href="pybase3.utils.md#SmartDict">pybase3.utils.SmartDict</a>:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><span class="code">dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><span class="code">list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</span></dd>
</dl>
<hr>
Methods inherited from <a href="builtins.md#dict">builtins.dict</a>:<br>
<dl><dt><a name="Record-__contains__"><strong>__contains__</strong></a>(self, key, /)</dt><dd><span class="code">True&nbsp;if&nbsp;the&nbsp;dictionary&nbsp;has&nbsp;the&nbsp;specified&nbsp;key,&nbsp;else&nbsp;False.</span></dd></dl>

<dl><dt><a name="Record-__delitem__"><strong>__delitem__</strong></a>(self, key, /)</dt><dd><span class="code">Delete&nbsp;self[key].</span></dd></dl>

<dl><dt><a name="Record-__eq__"><strong>__eq__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;self==value.</span></dd></dl>

<dl><dt><a name="Record-__ge__"><strong>__ge__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;self&gt;=value.</span></dd></dl>

<dl><dt><a name="Record-__getattribute__"><strong>__getattribute__</strong></a>(self, name, /)</dt><dd><span class="code">Return&nbsp;getattr(self,&nbsp;name).</span></dd></dl>

<dl><dt><a name="Record-__getitem__"><strong>__getitem__</strong></a>(...)</dt><dd><span class="code">x.<a href="#Record-__getitem__">__getitem__</a>(y)&nbsp;&lt;==&gt;&nbsp;x[y]</span></dd></dl>

<dl><dt><a name="Record-__gt__"><strong>__gt__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;self&gt;value.</span></dd></dl>

<dl><dt><a name="Record-__ior__"><strong>__ior__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;self|=value.</span></dd></dl>

<dl><dt><a name="Record-__iter__"><strong>__iter__</strong></a>(self, /)</dt><dd><span class="code">Implement&nbsp;iter(self).</span></dd></dl>

<dl><dt><a name="Record-__le__"><strong>__le__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;self&lt;=value.</span></dd></dl>

<dl><dt><a name="Record-__len__"><strong>__len__</strong></a>(self, /)</dt><dd><span class="code">Return&nbsp;len(self).</span></dd></dl>

<dl><dt><a name="Record-__lt__"><strong>__lt__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;self&lt;value.</span></dd></dl>

<dl><dt><a name="Record-__ne__"><strong>__ne__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;self!=value.</span></dd></dl>

<dl><dt><a name="Record-__or__"><strong>__or__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;self|value.</span></dd></dl>

<dl><dt><a name="Record-__reversed__"><strong>__reversed__</strong></a>(self, /)</dt><dd><span class="code">Return&nbsp;a&nbsp;reverse&nbsp;iterator&nbsp;over&nbsp;the&nbsp;dict&nbsp;keys.</span></dd></dl>

<dl><dt><a name="Record-__ror__"><strong>__ror__</strong></a>(self, value, /)</dt><dd><span class="code">Return&nbsp;value|self.</span></dd></dl>

<dl><dt><a name="Record-__setitem__"><strong>__setitem__</strong></a>(self, key, value, /)</dt><dd><span class="code">Set&nbsp;self[key]&nbsp;to&nbsp;value.</span></dd></dl>

<dl><dt><a name="Record-__sizeof__"><strong>__sizeof__</strong></a>(...)</dt><dd><span class="code">D.<a href="#Record-__sizeof__">__sizeof__</a>()&nbsp;-&gt;&nbsp;size&nbsp;of&nbsp;D&nbsp;in&nbsp;memory,&nbsp;in&nbsp;bytes</span></dd></dl>

<dl><dt><a name="Record-clear"><strong>clear</strong></a>(...)</dt><dd><span class="code">D.<a href="#Record-clear">clear</a>()&nbsp;-&gt;&nbsp;None.&nbsp;&nbsp;Remove&nbsp;all&nbsp;items&nbsp;from&nbsp;D.</span></dd></dl>

<dl><dt><a name="Record-get"><strong>get</strong></a>(self, key, default=None, /)</dt><dd><span class="code">Return&nbsp;the&nbsp;value&nbsp;for&nbsp;key&nbsp;if&nbsp;key&nbsp;is&nbsp;in&nbsp;the&nbsp;dictionary,&nbsp;else&nbsp;default.</span></dd></dl>

<dl><dt><a name="Record-items"><strong>items</strong></a>(...)</dt><dd><span class="code">D.<a href="#Record-items">items</a>()&nbsp;-&gt;&nbsp;a&nbsp;set-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;providing&nbsp;a&nbsp;view&nbsp;on&nbsp;D's&nbsp;items</span></dd></dl>

<dl><dt><a name="Record-keys"><strong>keys</strong></a>(...)</dt><dd><span class="code">D.<a href="#Record-keys">keys</a>()&nbsp;-&gt;&nbsp;a&nbsp;set-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;providing&nbsp;a&nbsp;view&nbsp;on&nbsp;D's&nbsp;keys</span></dd></dl>

<dl><dt><a name="Record-pop"><strong>pop</strong></a>(...)</dt><dd><span class="code">D.<a href="#Record-pop">pop</a>(k[,d])&nbsp;-&gt;&nbsp;v,&nbsp;remove&nbsp;specified&nbsp;key&nbsp;and&nbsp;return&nbsp;the&nbsp;corresponding&nbsp;value.<br>
&nbsp;<br>
If&nbsp;the&nbsp;key&nbsp;is&nbsp;not&nbsp;found,&nbsp;return&nbsp;the&nbsp;default&nbsp;if&nbsp;given;&nbsp;otherwise,<br>
raise&nbsp;a&nbsp;KeyError.</span></dd></dl>

<dl><dt><a name="Record-popitem"><strong>popitem</strong></a>(self, /)</dt><dd><span class="code">Remove&nbsp;and&nbsp;return&nbsp;a&nbsp;(key,&nbsp;value)&nbsp;pair&nbsp;as&nbsp;a&nbsp;2-tuple.<br>
&nbsp;<br>
Pairs&nbsp;are&nbsp;returned&nbsp;in&nbsp;LIFO&nbsp;(last-in,&nbsp;first-out)&nbsp;order.<br>
Raises&nbsp;KeyError&nbsp;if&nbsp;the&nbsp;dict&nbsp;is&nbsp;empty.</span></dd></dl>

<dl><dt><a name="Record-setdefault"><strong>setdefault</strong></a>(self, key, default=None, /)</dt><dd><span class="code">Insert&nbsp;key&nbsp;with&nbsp;a&nbsp;value&nbsp;of&nbsp;default&nbsp;if&nbsp;key&nbsp;is&nbsp;not&nbsp;in&nbsp;the&nbsp;dictionary.<br>
&nbsp;<br>
Return&nbsp;the&nbsp;value&nbsp;for&nbsp;key&nbsp;if&nbsp;key&nbsp;is&nbsp;in&nbsp;the&nbsp;dictionary,&nbsp;else&nbsp;default.</span></dd></dl>

<dl><dt><a name="Record-update"><strong>update</strong></a>(...)</dt><dd><span class="code">D.<a href="#Record-update">update</a>([E,&nbsp;]**F)&nbsp;-&gt;&nbsp;None.&nbsp;&nbsp;Update&nbsp;D&nbsp;from&nbsp;dict/iterable&nbsp;E&nbsp;and&nbsp;F.<br>
If&nbsp;E&nbsp;is&nbsp;present&nbsp;and&nbsp;has&nbsp;a&nbsp;.<a href="#Record-keys">keys</a>()&nbsp;method,&nbsp;then&nbsp;does:&nbsp;&nbsp;for&nbsp;k&nbsp;in&nbsp;E:&nbsp;D[k]&nbsp;=&nbsp;E[k]<br>
If&nbsp;E&nbsp;is&nbsp;present&nbsp;and&nbsp;lacks&nbsp;a&nbsp;.<a href="#Record-keys">keys</a>()&nbsp;method,&nbsp;then&nbsp;does:&nbsp;&nbsp;for&nbsp;k,&nbsp;v&nbsp;in&nbsp;E:&nbsp;D[k]&nbsp;=&nbsp;v<br>
In&nbsp;either&nbsp;case,&nbsp;this&nbsp;is&nbsp;followed&nbsp;by:&nbsp;for&nbsp;k&nbsp;in&nbsp;F:&nbsp;&nbsp;D[k]&nbsp;=&nbsp;F[k]</span></dd></dl>

<dl><dt><a name="Record-values"><strong>values</strong></a>(...)</dt><dd><span class="code">D.<a href="#Record-values">values</a>()&nbsp;-&gt;&nbsp;an&nbsp;<a href="builtins.md#object">object</a>&nbsp;providing&nbsp;a&nbsp;view&nbsp;on&nbsp;D's&nbsp;values</span></dd></dl>

<hr>
Class methods inherited from <a href="builtins.md#dict">builtins.dict</a>:<br>
<dl><dt><a name="Record-__class_getitem__"><strong>__class_getitem__</strong></a>(...)<span class="grey"><span class="heading-text"> from <a href="builtins.md#type">builtins.type</a></span></span></dt><dd><span class="code">See&nbsp;<a href="https://peps.python.org/pep-0585/">PEP&nbsp;585</a></span></dd></dl>

<dl><dt><a name="Record-fromkeys"><strong>fromkeys</strong></a>(iterable, value=None, /)<span class="grey"><span class="heading-text"> from <a href="builtins.md#type">builtins.type</a></span></span></dt><dd><span class="code">Create&nbsp;a&nbsp;new&nbsp;dictionary&nbsp;with&nbsp;keys&nbsp;from&nbsp;iterable&nbsp;and&nbsp;values&nbsp;set&nbsp;to&nbsp;value.</span></dd></dl>

<hr>
Static methods inherited from <a href="builtins.md#dict">builtins.dict</a>:<br>
<dl><dt><a name="Record-__new__"><strong>__new__</strong></a>(*args, **kwargs)<span class="grey"><span class="heading-text"> from <a href="builtins.md#type">builtins.type</a></span></span></dt><dd><span class="code">Create&nbsp;and&nbsp;return&nbsp;a&nbsp;new&nbsp;<a href="builtins.md#object">object</a>.&nbsp;&nbsp;See&nbsp;help(type)&nbsp;for&nbsp;accurate&nbsp;signature.</span></dd></dl>

<hr>
Data and other attributes inherited from <a href="builtins.md#dict">builtins.dict</a>:<br>
<dl><dt><strong>__hash__</strong> = None</dl>

</td></tr></table></td></tr></table><p>
<table class="section">
<tr class="decor functions-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><strong class="bigsection">Functions</strong></td></tr>
    
<tr><td class="decor functions-decor"><span class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td><td>&nbsp;</td>
<td class="singlecolumn"><dl><dt><a name="-Lock"><strong>Lock</strong></a> = allocate_lock(...)</dt><dd><span class="code">allocate_lock()&nbsp;-&gt;&nbsp;lock&nbsp;<a href="builtins.md#object">object</a><br>
(allocate()&nbsp;is&nbsp;an&nbsp;obsolete&nbsp;synonym)<br>
&nbsp;<br>
Create&nbsp;a&nbsp;new&nbsp;lock&nbsp;<a href="builtins.md#object">object</a>.&nbsp;See&nbsp;help(type(threading.<a href="#-Lock">Lock</a>()))&nbsp;for<br>
information&nbsp;about&nbsp;locks.</span></dd></dl>
 <dl><dt><a name="-connect"><strong>connect</strong></a>(dirname: str)</dt><dd><span class="code">Returns&nbsp;a&nbsp;<a href="#Connection">Connection</a>&nbsp;<a href="builtins.md#object">object</a>&nbsp;for&nbsp;the&nbsp;specified&nbsp;directory.</span></dd></dl>
 <dl><dt><strong>getDay</strong> <em>lambda</em> (...)</dt></dl>
 <dl><dt><strong>getMonth</strong> <em>lambda</em> (...)</dt></dl>
 <dl><dt><strong>getYear</strong> <em>lambda</em> (...)</dt><dd><span class="code">#&nbsp;getYear&nbsp;=&nbsp;lambda:&nbsp;datetime.now().year&nbsp;-&nbsp;1900</span></dd></dl>
 <dl><dt><a name="-make_bottomline"><strong>make_bottomline</strong></a>(linetype: str, description: List[Tuple[int, str, str, str, int, int]]) -&gt; str</dt><dd><span class="code">Returns&nbsp;the&nbsp;bottom&nbsp;line&nbsp;of&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;of&nbsp;the&nbsp;type&nbsp;specified&nbsp;by&nbsp;linetype</span></dd></dl>
 <dl><dt><a name="-make_csv_lines"><strong>make_csv_lines</strong></a>(curr: pybase3.Cursor) -&gt; Generator[str, NoneType, NoneType]</dt><dd><span class="code">Generates&nbsp;all&nbsp;the&nbsp;lines&nbsp;for&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;,&nbsp;'csv'&nbsp;style</span></dd></dl>
 <dl><dt><a name="-make_cursor_line"><strong>make_cursor_line</strong></a>(linetype: str, r: pybase3.Record, description: List[Tuple[int, str, str, str, int, int]]) -&gt; str</dt><dd><span class="code">Returns&nbsp;a&nbsp;data&nbsp;line&nbsp;(field&nbsp;values)&nbsp;of&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;of&nbsp;the&nbsp;type&nbsp;specified&nbsp;by&nbsp;linetype</span></dd></dl>
 <dl><dt><a name="-make_cursor_lines"><strong>make_cursor_lines</strong></a>(linetype: str, curr: pybase3.Cursor) -&gt; Generator[str, NoneType, NoneType]</dt><dd><span class="code">Generates&nbsp;all&nbsp;the&nbsp;lines&nbsp;for&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;of&nbsp;the&nbsp;type&nbsp;specified&nbsp;by&nbsp;linetype</span></dd></dl>
 <dl><dt><a name="-make_header_line"><strong>make_header_line</strong></a>(linetype: str, description: List[Tuple[int, str, str, str, int, int]]) -&gt; str</dt><dd><span class="code">Returns&nbsp;the&nbsp;header&nbsp;line&nbsp;(field&nbsp;names)&nbsp;of&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;of&nbsp;the&nbsp;type&nbsp;specified&nbsp;by&nbsp;linetype</span></dd></dl>
 <dl><dt><a name="-make_intermediateline"><strong>make_intermediateline</strong></a>(linetype: str, description: List[Tuple[int, str, str, str, int, int]]) -&gt; str</dt><dd><span class="code">Returns&nbsp;the&nbsp;intermediate&nbsp;(line&nbsp;joiner)&nbsp;line&nbsp;of&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;of&nbsp;the&nbsp;type&nbsp;specified&nbsp;by&nbsp;linetype</span></dd></dl>
 <dl><dt><a name="-make_list_lines"><strong>make_list_lines</strong></a>(curr: pybase3.Cursor) -&gt; Generator[str, NoneType, NoneType]</dt></dl>
 <dl><dt><a name="-make_pretty_table_lines"><strong>make_pretty_table_lines</strong></a>(curr: pybase3.Cursor) -&gt; Generator[str, NoneType, NoneType]</dt><dd><span class="code">Generates&nbsp;all&nbsp;the&nbsp;lines&nbsp;for&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;,&nbsp;'box&nbsp;lines'&nbsp;style</span></dd></dl>
 <dl><dt><a name="-make_raw_lines"><strong>make_raw_lines</strong></a>(curr: pybase3.Cursor) -&gt; Generator[str, NoneType, NoneType]</dt><dd><span class="code">Generates&nbsp;all&nbsp;the&nbsp;lines&nbsp;for&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;,&nbsp;'raw'&nbsp;(no&nbsp;separators)&nbsp;style</span></dd></dl>
 <dl><dt><a name="-make_table_lines"><strong>make_table_lines</strong></a>(curr: pybase3.Cursor) -&gt; Generator[str, NoneType, NoneType]</dt><dd><span class="code">Generates&nbsp;all&nbsp;the&nbsp;lines&nbsp;for&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;,&nbsp;'sqlite3&nbsp;.table'&nbsp;style</span></dd></dl>
 <dl><dt><a name="-make_topline"><strong>make_topline</strong></a>(linetype: str, description: List[Tuple[int, str, str, str, int, int]]) -&gt; str</dt><dd><span class="code">Returns&nbsp;the&nbsp;top&nbsp;line&nbsp;of&nbsp;a&nbsp;table-like&nbsp;<a href="builtins.md#object">object</a>&nbsp;of&nbsp;the&nbsp;type&nbsp;specified&nbsp;by&nbsp;linetype</span></dd></dl>
 <dl><dt><strong>to_bytes</strong> <em>lambda</em> x</dt></dl>
 <dl><dt><strong>to_str</strong> <em>lambda</em> x</dt></dl>
</td></tr></table><p>
<table class="section">
<tr class="decor data-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><strong class="bigsection">Data</strong></td></tr>
    
<tr><td class="decor data-decor"><span class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td><td>&nbsp;</td>
<td class="singlecolumn"><strong>AnyStr</strong> = ~AnyStr<br>
<strong>Callable</strong> = typing.Callable<br>
<strong>Generator</strong> = typing.Generator<br>
<strong>List</strong> = typing.List<br>
<strong>Tuple</strong> = typing.Tuple<br>
<strong>__description__</strong> = 'A simple library to read and write dbase III files.'<br>
<strong>__email__</strong> = 'esavoretti@gmail.com'<br>
<strong>__license__</strong> = 'MIT'<br>
<strong>__url__</strong> = 'https://github.com/sandy98/pybase3'<br>
<strong>bottomlines</strong> = {'csv': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'line': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'list': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'pretty_table': {'join': '┴', 'left': '└', 'line': '─', 'right': '┘'}, 'table': {'join': '+', 'left': '+', 'line': '-', 'right': '+'}}<br>
<strong>separators</strong> = {'csv': ',', 'line': ' ', 'list': '|', 'pretty_table': '│', 'table': '|'}<br>
<strong>seplines</strong> = {'csv': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'line': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'list': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'pretty_table': {'join': '┼', 'left': '├', 'line': '─', 'right': '┤'}, 'table': {'join': '+', 'left': '+', 'line': '-', 'right': '+'}}<br>
<strong>toplines</strong> = {'csv': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'line': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'list': {'join': ' ', 'left': ' ', 'line': ' ', 'right': ' '}, 'pretty_table': {'join': '┬', 'left': '┌', 'line': '─', 'right': '┐'}, 'table': {'join': '+', 'left': '+', 'line': '-', 'right': '+'}}</td></tr></table><p>
<table class="section">
<tr class="decor author-decor heading-text">
<td class="section-title" colspan=3>&nbsp;<br><strong class="bigsection">Author</strong></td></tr>
    
<tr><td class="decor author-decor"><span class="code">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td><td>&nbsp;</td>
<td class="singlecolumn">Domingo&nbsp;fE.&nbsp;Savoretti</td></tr></table>
</body></html>