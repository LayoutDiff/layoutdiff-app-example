import 'package:flutter/material.dart';

void main() => runApp(LayoutDiffExample());

class _BoxDecorationState extends State<LayoutDiffBoxDecoration> {
  final List<MaterialColor> _bgColors = [Colors.blue, Colors.green, Colors.yellow, Colors.red, Colors.brown];
  int _bgColorIndex = 0;
  MaterialColor _bgColor = Colors.blue;


  MaterialColor getBgColor<T>() {
    var color =_bgColors[_bgColorIndex];

    _bgColorIndex += 1;

    if(_bgColorIndex >= _bgColors.length) {
      _bgColorIndex = 0;
    }

    return color;
  }
  
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [_bgColor[100], _bgColor[500]]
        )
      ),
      child: ListView(
          padding: const EdgeInsets.all(20),
          children: <Widget>[
            Center(
              child: Text('LayoutDiff is cool!',
                style: TextStyle(
                  fontSize: 35,
                  color: Colors.white,
                ),
              ),
            ),
            ElevatedButton(            
              child: Text('Press'),
              onPressed: () {  
                setState(() {
                  _bgColor = getBgColor();
                });
              },
            )
          ]
      )
    );
  }

}

class LayoutDiffBoxDecoration extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _BoxDecorationState();
  }

}

class LayoutDiffExample extends StatelessWidget {

   @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'LayoutDiff Example',
      home: Scaffold(
        appBar: AppBar(
          title: Text('LayoutDiff Example.'),
        ),
        body: LayoutDiffBoxDecoration()
      ),
    );
  }

}
