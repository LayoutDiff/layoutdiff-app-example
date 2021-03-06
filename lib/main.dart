import 'package:flutter/material.dart';

void main() => runApp(LayoutDiffExample());

class LayoutDiffExample extends StatelessWidget {

   @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'LayoutDiff Example',
      home: Scaffold(
        appBar: AppBar(
          title: Text('LayoutDiff Example.'),
        ),
        body: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [Colors.yellow[100], Colors.yellow[500]]
            )
          ),
          child: Center(
            child: Text('LayoutDiff is cool!',
              style: TextStyle(
                fontSize: 35,
                color: Colors.white,
              ),
            ),
          ),
        ),
      ),
    );
  }

}
